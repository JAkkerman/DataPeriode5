#!/usr/bin/env python
# Name: Joos Akkerman
# Student number: 11304723
"""
This script converts data obtained from a .csv file to JSON format
"""

import json
import numpy as np
import csv
import pandas as pd

INPUT_CSV = "worldbank_GDPdata.csv"
OUTPUT_JSON = "worldbank_GDPdata.json"
INDEX = "year"
ORIENT = "Country Name"
SELECTED_ROWS = "Japan"

def clean(input):
    """
    Reads the csv file and collects the needed data
    """

    input = pd.read_csv(INPUT_CSV)
    data = {}
    for i in range(1960, 2018):
        data[str(i)] = input.loc[117, str(i)]
    print(data)

    return data


def convert(data, index, orient, outputJSON):
    """
    Converts selected data to JSON format
    """

    with open(outputJSON, 'w') as output:
        output.write(json.dumps(data))


if __name__ == '__main__':
    # read data from data file
    data = clean(INPUT_CSV)

    # convert data to JSON format
    convert(data, INDEX, ORIENT, OUTPUT_JSON)
