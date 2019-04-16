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
    cleans the relevant data
    """

    # open csv file and edit data
    data = pd.read_csv(datafile)
    data.replace('', np.nan)

    num_catergories = [pop_dens, inf_mort, GDP_cap]

    # select only the relevant columns
    data = data[["Country", "Region", pop_dens, inf_mort, GDP_cap]]

    # clean region data (delete excess spaces)
    for value in data["Region"]:
        data["Region"] = data["Region"].replace(value, ' '.join(value.split()))

    # clean population density data
    data[pop_dens] = data[pop_dens].replace('unknown', np.nan)
    for value in data[pop_dens]:
        data[pop_dens] = data[pop_dens].replace(value, float(str(value).replace(",", ".")))

    # clean infant mortality data
    for value in data[inf_mort]:
        data[inf_mort] = data[inf_mort].replace(value, float(str(value).replace(",", ".")))

    # clean GDP per capita data
    data[GDP_cap] = data[GDP_cap].replace('unknown', float(np.nan))
    for value in data[GDP_cap]:
        if type(value) == str:
            data[GDP_cap] = data[GDP_cap].replace(value, int(''.join(i for i in value if i.isdigit())))

    return data


def getvalues(data):
    """
    calculates the mean, median, mode and standard deviation
    """

    # compute the mean, median and mode for GDP per capita and print
    mean_GDPCap = data[GDP_cap].mean(skipna=True)
    median_GDPCap = data[GDP_cap].median(skipna=True)
    mode_GDPCap = data[GDP_cap].mode()
    print(f"Mean of GDP per capita: {mean_GDPCap}")
    print(f"Median of GDP per capita: {median_GDPCap}")
    print(f"Mode of GDP per capita: {mode_GDPCap}")

    # compute the five number summary for infant mortality and print
    infmort_Min = data[inf_mort].min()
    infmort_FQuin = data[inf_mort].quantile([0.25])
    infmort_Med = data[inf_mort].median()
    infmort_TQuin = data[inf_mort].quantile([0.75])
    infmort_Max = data[inf_mort].max()
    print(f"Minimum amount of child mortality: {infmort_Min}")
    print(f"First quartile of child mortality: {infmort_FQuin}")
    print(f"Median of child mortality: {infmort_Med}")
    print(f"Third quartile of child mortality: {infmort_TQuin}")
    print(f"Maximum amount of child mortality: {infmort_Max}")


def plotGDP(data):
    """
    plots a histogram showing GDP data
    """

    plt.grid()
    plt.hist(data[GDP_cap], bins = 1000)
    plt.title('Distribution of GDP per capita')
    plt.ylabel('Amount of countries')
    plt.xlabel('GDP per capita')
    plt.xlim([0, 50000])
    plt.yticks(range(0, 21))
    plt.show()


def plotInfMort(data):
    """
    plots a boxplot showing infant mortality data
    """

    boxplot = data.boxplot(column = [inf_mort])
    plt.title("Distribution of Infant Mortality (per 1000 births)")
    plt.ylabel("Infant Mortality")
    plt.xlabel("")
    plt.show()


def convert(data):
    """
    sets up datafile in json format
    """
    data = data.set_index("Country").to_json("data.json", orient='index')


if __name__ == "__main__":
    # clean data to make it usable
    CLEANED_DATA = cleandata(INPUT_CSV)

    # get relevant data
    mean_GDPCap = getvalues(CLEANED_DATA)

    # plot a histogram analyzing GDP data
    plotGDP(CLEANED_DATA)

    # plot a boxplot analyzing infant mortality data
    plotInfMort(CLEANED_DATA)

    # convert to json file
    convert(CLEANED_DATA)
