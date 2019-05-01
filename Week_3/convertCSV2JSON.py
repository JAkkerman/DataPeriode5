#!/usr/bin/env python
# Name: Joos Akkerman
# Student number: 11304723
"""
This script converts data obtained from a .csv file to JSON format
"""

import json
import pandas as pd

INPUT_CSV = "worldbank_GDPdata.csv"
OUTPUT_JSON = "worldbank_GDPdata.json"
SELECTED_ROW = 117
FIRSTCOLUMN = 1960
LASTCOLUMN = 2018


def clean(input, selected_row, firstcolumn, lastcolumn):
    """
    Reads the csv file and returns the requested data
    """

    input = pd.read_csv(INPUT_CSV)
    data = {}
    for i in range(firstcolumn, lastcolumn):
        data[str(i)] = input.loc[selected_row, str(i)]

    return data


def convert(data, outputJSON):
    """
    Converts selected data to JSON format
    """

    with open(outputJSON, 'w') as output:
        output.write(json.dumps(data))


if __name__ == '__main__':
    # read data from data file
    data = clean(INPUT_CSV, SELECTED_ROW, FIRSTCOLUMN, LASTCOLUMN)

    # convert data to JSON format
    convert(data, OUTPUT_JSON)
