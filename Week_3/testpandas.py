import json
import numpy as np
import csv
import pandas as pd


# INPUT_CSV = r"C:\Users\juliu\OneDrive\Documenten\GitHub\DataPeriode5\Week_3\worldbank_GDPdata.csv"
INPUT_CSV = "worldbank_GDPdata.csv"
# OUTPUT_JSON = r"C:\Users\juliu\OneDrive\Documenten\GitHub\DataPeriode5\Week_3\worldbank_GDPdata.json"
OUTPUT_JSON = "worldbank_GDPdata.json"
INDEX = "year"
ORIENT = "Country Name"
SELECTED_ROWS = "Japan"

# def clean(input, country):
#     """
#     Reads the csv file and collects the needed data
#     """
#     rawdata = csv.DictReader(open(input))
#     data = []
#     for row in rawdata:
#         if row['Country Name'] == country:
#             data.append(row)
#
#     return data


# def convert(data, index, orient, outputJSON):
#     """
#     Converts selected data to JSON format
#     """
#
#     with open(outputJSON, 'w') as output:
#         output.write('[')
#         commas = len(data)
#         for entry in data:
#             print(entry)
#             output.write(json.dumps(entry))
#             if commas > 1:
#                 output.write(',')
#             commas = commas - 1
#         output.write(']')


if __name__ == '__main__':
    # read data from data file
    data = pd.read_csv(INPUT_CSV)
    # print('this is the data')
    # print(data)

    # subdata = data.loc[117, ['Country Name']]

    JPN_data = ['Country Name']
    for i in range(1960, 2018):
        JPN_data.append(str(i))

        # JPN_data.append({str(i): data.loc[117, str(i)]})
    print(JPN_data)

    subdata = data.loc[117, JPN_data]
    print('this is your subdata')
    print(subdata)

    subdata.to_json("worldbank_GDPdata.json")
    # dataJPN = [117]
    # dataJPN.append(JPN_data)
    # print(dataJPN)
    #
    # for b in dataJPN:
        # b =117
        # b = []
        # print(b)
        # subdata = data[dataJPN]
    # print('this is the subdata')
    # print(subdata)

    'joos, gebruik set index, net als bij eda.py, om de hoofd colom voor je json file te selecteren'
    # convert data to JSON format
    # convert(data, INDEX, ORIENT, OUTPUT_JSON)
