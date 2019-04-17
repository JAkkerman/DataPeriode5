#!/usr/bin/env python
# Name: Joos Akkerman
# Student number: 11304723
"""
This script graphically visualizes data obtained from a .csv file and stores it in a JSON-file
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

INPUT_CSV = "input.csv"
pop_dens = "Pop. Density (per sq. mi.)"
inf_mort = "Infant mortality (per 1000 births)"
GDP_cap = "GDP ($ per capita) dollars"

def cleandata(datafile):
    """
    Cleans data for the following relevant columns:
    - "Country"
    - "Region"
    - "Pop. Density (per sq. mi.)"
    - "Infant mortality (per 1000 births)"
    - "GDP ($ per capita) dollars"
    """

    # open csv file, select relevant columns, replace 'unknown' by NaN, replace commas by dots
    data = pd.read_csv(datafile)
    data = data[["Country", "Region", pop_dens, inf_mort, GDP_cap]]
    data = data.replace('unknown', np.nan)
    data = data.replace(',', '.', regex=True)

    # GDP data for Suriname is factually incorrect, therefore it is deleted from the data set
    data.at[193, GDP_cap] = np.nan

    # clean country and region data of excess spaces
    data["Country"] = data["Country"].str.strip()
    data["Region"] = data["Region"].str.strip()

    # delete dollar addition from GDP per capita data
    data[GDP_cap] = data[GDP_cap].str.strip(" dollars")

    # change infant mortality, population density and GDP per capita data to floats
    data[[inf_mort, pop_dens, GDP_cap]] = data[[inf_mort, pop_dens, GDP_cap]].astype(float)

    return data


def getvalues(data):
    """
    Calculates the mean, median and mode of GDP per capita data and Five Numbers
    Summary of infant mortality data
    """

    # compute values for GDP per capita and print
    print("Mean, Median and Mode of worldwide GDP per capita:")
    print(f"Mean of GDP per capita: {int(data[GDP_cap].mean(skipna=True))}")
    print(f"Median of GDP per capita: {data[GDP_cap].median(skipna=True)}")
    print(f"Mode of GDP per capita: {data[GDP_cap].mode()[0]}")
    print(f"Standard deviation of GDP per capita: {data[GDP_cap].std()}")
    print()

    # compute values for infant mortality and print
    print("Five number summary for Infant Mortality Rate per Country:")
    print(f"Minimum: {data[inf_mort].min()}")
    print(f"Q1: {data[inf_mort].quantile(q = 0.25)}")
    print(f"Median: {data[inf_mort].median()}")
    print(f"Q3: {data[inf_mort].quantile(q = 0.75)}")
    print(f"Maximum: {data[inf_mort].max()}")


def plotGDP(data):
    """
    Plots a histogram showing GDP per capita data
    """

    data[GDP_cap].plot.hist(bins=100)
    plt.grid()
    plt.title('Distribution of GDP per capita')
    plt.ylabel('Amount of countries')
    plt.xlabel('GDP per capita')
    plt.axis([0, 60000, 0, 28])
    plt.show()


def plotInfMort(data):
    """
    Plots a boxplot showing overall infant mortality data and per region
    """

    # plots boxplot of overall infant mortality
    data.boxplot(column = [inf_mort])
    plt.title("Distribution of Infant Mortality (per 1000 births)")
    plt.ylabel("Infant Mortality")

    plt.show()

    # plots boxplot of infant mortality per region
    data.boxplot(column=[inf_mort], by="Region")
    plt.suptitle("")
    plt.xticks(rotation=80)
    plt.title("Distribution of Infant Mortality (per 1000 births) per region")
    plt.ylabel("Infant Mortality")

    plt.show()


def convert(data):
    """
    Sets up datafile in json format
    """

    data = data.set_index("Country").to_json("data.json", orient='index')


if __name__ == "__main__":

    # clean data to make it usable
    CLEANED_DATA = cleandata(INPUT_CSV)

    # get relevant data
    mean_GDPCap = getvalues(CLEANED_DATA)

    # plot a histogram analyzing GDP data
    plotGDP(CLEANED_DATA)

    # plot boxplots analyzing infant mortality data
    plotInfMort(CLEANED_DATA)

    # convert to json file
    convert(CLEANED_DATA)
