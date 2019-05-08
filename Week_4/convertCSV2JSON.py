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
FIRSTCOLUMN = 1
LASTCOLUMN = 6


def clean(input, selected_rows, firstcolumn, lastcolumn):
    """
    Reads the csv file and returns the requested data
    """

    input = pd.read_csv(INPUT_CSV)
    data = []
    for selected_row in selected_rows:

        subdata = {"LOCATION": input.loc[selected_row, "LOCATION"],
                        "%RENEW": input.loc[selected_row, "Value"].item()}
        data.append(subdata)

    return data

def sort(data):
    """
    Sorts data from low to high, using bubble sort
    """

    lendata = len(data)

    for i in range(lendata):
        for j in range(0, lendata-i-1):
            if data[j]["%RENEW"] > data[j+1]["%RENEW"]:
                data[j], data[j+1] = data[j+1], data[j]

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

    # sort data (low to high value)
    data = sort(data)

    # convert data to JSON format
    convert(data, OUTPUT_JSON)
