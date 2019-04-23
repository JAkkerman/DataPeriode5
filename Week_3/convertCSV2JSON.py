#!/usr/bin/env python
# Name: Joos Akkerman
# Student number: 11304723
"""
This script converts data obtained from a .csv file to JSON format
"""

import pandas as pd
import json

# INPUT_CSV = r"C:\Users\juliu\OneDrive\Documenten\GitHub\DataPeriode5\Week_3\worldbank_GDPdata.csv"
INPUT_CSV = "worldbank_GDPdata.csv"
OUTPUT_JSON = "imf_GDPdata.json"
INDEX = "year"
ORIENT = "index"
SELECTED_ROWS = ["Country Name", "Netherlands", "Venezuela", "Japan", "Poland", "Saudi Arabia"]

def clean(input, rows):
    """
    Reads the csv file and collects the needed data
    """

    data = pd.read_csv(input, sep=',')
    print(data)
    data = data[rows]

    print(data)

    return []


def convert(data, index, orient):
    """
    Converts selected data to JSON format
    """

    return []


if __name__ == '__main__':
    # read data from data file
    data = clean(INPUT_CSV, SELECTED_ROWS)

    # convert data to JSON format
    convert(data, INDEX, ORIENT)
