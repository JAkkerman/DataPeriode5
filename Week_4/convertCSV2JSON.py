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
SELECTED_ROWS = [2222, 2279, 2450, 2564, 2621, 2792, 3305, 3419, 3818, 3191]
FIRSTCOLUMN = 1
LASTCOLUMN = 6


def clean(input, selected_rows, firstcolumn, lastcolumn):
    """
    Reads the csv file and returns the requested data
    """

    input = pd.read_csv(INPUT_CSV)
    data = []
    id = 1
    subdata = {}
    for selected_row in selected_rows:

        subdata = {"LOCATION": input.loc[selected_row, "LOCATION"],
                        "%RENEW": input.loc[selected_row, "Value"].item()}
        # subdata["LOCATION"] = input.loc[selected_row, "LOCATION"]
        # subdata["%RENEW"] = input.loc[selected_row, "Value"].item()
        id = id + 1

        data.append(subdata)

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
