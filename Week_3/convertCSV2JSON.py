#!/usr/bin/env python
# Name: Joos Akkerman
# Student number: 11304723
"""
This script converts data obtained from a .csv file to JSON format
"""

import json
import numpy as np
import csv

# INPUT_CSV = r"C:\Users\juliu\OneDrive\Documenten\GitHub\DataPeriode5\Week_3\worldbank_GDPdata.csv"
INPUT_CSV = "worldbank_GDPdata.csv"
# OUTPUT_JSON = r"C:\Users\juliu\OneDrive\Documenten\GitHub\DataPeriode5\Week_3\worldbank_GDPdata.json"
OUTPUT_JSON = "worldbank_GDPdata.json"
INDEX = "year"
ORIENT = "Country Name"
SELECTED_ROWS = ["Netherlands", "Venezuela, RB", "Japan", "Poland", "Saudi Arabia"]

def clean(input, sel_rows):
    """
    Reads the csv file and collects the needed data
    """
    rawdata = csv.DictReader(open(input))
    data = []
    for row in rawdata:
        for country in sel_rows:
            if row['Country Name'] == country:
                data.append(row)

    return data


def convert(data, index, orient, outputJSON):
    """
    Converts selected data to JSON format
    """

    with open(outputJSON, 'w') as output:
        output.write('[')
        commas = len(data)
        for entry in data:
            print(entry)
            output.write(json.dumps(entry))
            if commas > 1:
                output.write(',')
            commas = commas - 1
        output.write(']')


if __name__ == '__main__':
    # read data from data file
    data = clean(INPUT_CSV, SELECTED_ROWS)

    # convert data to JSON format
    convert(data, INDEX, ORIENT, OUTPUT_JSON)
