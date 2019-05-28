#!/usr/bin/env python
# Name: Joos Akkerman
# Student number: 11304723
"""
This script converts data obtained from a .csv file to JSON format
"""

import json
import numpy as np
import pandas as pd

INPUT_CSV = "data.csv"
OUTPUT_JSON = "data.json"
FIRSTCOLUMN = 1
LASTCOLUMN = 6


def clean(input, firstcolumn, lastcolumn):
    """
    Reads the csv file and returns the requested data
    """

    input = pd.read_csv(INPUT_CSV, keep_default_na=False)
    countries = {}
    # for row in range(2109, 4218):
    #     countries[input.loc[row, 'LOCATION']] = {}
    #
    # for row in range(2109, 4218):
    #     countries[input.loc[row, 'LOCATION']][int(input.loc[row, 'TIME'])] = {'YEAR': int(input.loc[row, 'TIME']), "VALUE": input.loc[row, 'Value']}
    for row in range(2109, 4218):
        countries[input.loc[row, 'LOCATION']] = []

    for row in range(2109, 4218):
        countries[input.loc[row, 'LOCATION']].append({'YEAR': int(input.loc[row, 'TIME']), "VALUE": input.loc[row, 'Value']})

    return countries


def convert(data, outputJSON):
    """
    Converts selected data to JSON format
    """

    with open(outputJSON, 'w') as output:
        output.write(json.dumps(data))


if __name__ == '__main__':

    # read data from data file
    data = clean(INPUT_CSV, FIRSTCOLUMN, LASTCOLUMN)

    # convert data to JSON format
    convert(data, OUTPUT_JSON)
