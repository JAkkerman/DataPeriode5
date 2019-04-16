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
    """cleans the relevant data"""

    # open csv file and edit data
    data = pd.read_csv(datafile)
    data.replace('', np.nan)
    data.replace(',', '.')

    num_catergories = [pop_dens, inf_mort, GDP_cap]

    # clean population density data
    data[pop_dens] = data[pop_dens].replace('unknown', np.nan)
    for value in data[pop_dens]:
        data[pop_dens] = data[pop_dens].replace(value, float(str(value).replace(",", ".")))
    # print(data[pop_dens])

    # clean infant mortality data
    for value in data[inf_mort]:
        data[inf_mort] = data[inf_mort].replace(value, float(str(value).replace(",", ".")))
    # print(data[inf_mort])

    # clean GDP per capita data
    data[GDP_cap] = data[GDP_cap].replace('unknown', float(np.nan))
    for value in data[GDP_cap]:
        if type(value) == str:
            data[GDP_cap] = data[GDP_cap].replace(value, int(''.join(i for i in value if i.isdigit())))
    # print(data[GDP_cap])

    return data

def getvalues(data):
    """calculates the mean, median, mode and standard deviation"""

    # calculate the means
    # print(data[pop_dens].mean(skipna=True))
    mean_PopDens = data[pop_dens].mean(skipna=True)
    # print(data[inf_mort].mean(skipna=True))
    mean_InfMort = data[inf_mort].mean(skipna=True)
    # print(data[GDP_cap].mean(skipna=True))
    mean_GDPCap = data[GDP_cap].mean(skipna=True)

    # calculate the medians
    # print(data[pop_dens].median(skipna=True))
    median_PopDens = data[pop_dens].median(skipna=True)
    # print(data[inf_mort].median(skipna=True))
    median_InfMort = data[inf_mort].median(skipna=True)
    # print(data[GDP_cap].median(skipna=True))
    median_GDPCap = data[GDP_cap].median(skipna=True)

    #calculate the modes
    # print(data[pop_dens].mode())
    mode_PopDens = data[pop_dens].mode()
    # print(data[inf_mort].mode())
    mode_InfMort = data[inf_mort].mode()
    # print(data[GDP_cap].mode())
    mode_GDPCap = data[GDP_cap].mode()

    # calculate the standard deviations
    print(np.std(data[pop_dens]))
    # stddev_PopDens = data[pop_dens].std(skipna=True)
    print(np.std(data[inf_mort]))
    # median_InfMort = data[inf_mort].median(skipna=True)
    print(np.std(data[GDP_cap]))
    # median_GDPCap = data[GDP_cap].median(skipna=True)

    return mean_GDPCap

def plotGDP(data):
    """ plots a histogram showing GDP data """

    plt.grid()
    plt.hist(data[GDP_cap], bins = 1000)
    plt.title('Distribution of GDP per capita')
    plt.ylabel('Amount of countries')
    plt.xlabel('GDP per capita')
    plt.xlim([0, 50000])
    plt.yticks(range(0, 21))
    plt.show()

def plotInfMort(data):
    """ plots a boxplot showing infant mortality data """

    print(data[inf_mort])
    plt.boxplot(data[inf_mort])
    plt.show()
    # boxplot = data.boxplot(column = [inf_mort])

if __name__ == "__main__":
    # clean data to make it usable
    CLEANED_DATA = cleandata(INPUT_CSV)

    # get relevant data
    mean_GDPCap = getvalues(CLEANED_DATA)

    # plot a histogram analyzing GDP data
    plotGDP(CLEANED_DATA)

    # plot a boxplot analyzing infant mortality data
    plotInfMort(CLEANED_DATA)
