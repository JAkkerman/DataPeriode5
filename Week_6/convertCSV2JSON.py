#!/usr/bin/env python
# Name: Joos Akkerman
# Student number: 11304723
"""
This script converts data obtained from a .csv file to JSON format
"""

import json
import pandas as pd

INPUT_CSV = "data.csv"
OUTPUT_JSON = "data.json"
SELECTED_ROWS = [2222, 2336, 2507, 2678, 2735, 2849, 2906, 2393, 2279, 2450, 2564, 2621, 2792, 3305, 3419, 3818, 3191]
STARTYEAR = 1980
ENDYEAR = 2016
FIRSTCOLUMN = 1
LASTCOLUMN = 6


def clean(input, selected_rows, firstcolumn, lastcolumn):
    """
    Reads the csv file and returns the requested data
    """

    input = pd.read_csv(INPUT_CSV)
    data = []
    countries = {}
    for row in range(2109, 4218):
        countries[input.loc[row, 'LOCATION']] = {}

    for row in range(2109, 4218):
        countries[input.loc[row, 'LOCATION']][int(input.loc[row, 'TIME'])] = input.loc[row, 'Value']

    data.append(countries)

    return data


def convert(data, outputJSON):
    """
    Converts selected data to JSON format
    """

    with open(outputJSON, 'w') as output:
        output.write(json.dumps(data))


if __name__ == '__main__':
    # read data from data file
    data = clean(INPUT_CSV, SELECTED_ROWS, FIRSTCOLUMN, LASTCOLUMN)

    # convert data to JSON format
    convert(data, OUTPUT_JSON)
