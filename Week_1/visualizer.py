#!/usr/bin/env python
# Name: Joos Akkerman
# Student number: 11304723
"""
This script visualizes data obtained from a .csv file
"""

import csv
import matplotlib.pyplot as plt

# Global constants for the input file, first and last year
INPUT_CSV = "movies.csv"
START_YEAR = 2008
END_YEAR = 2018

# Global dictionary for the data
data_dict = {str(key): [] for key in range(START_YEAR, END_YEAR)}

# collect data from release years
with open('movies.csv', newline='') as moviesfile:
    moviesreader = csv.reader(moviesfile)
    for row in moviesreader:
        if row[2].isdigit():
            data_dict[f"{row[2]}"].append(float(row[1]))

# calculate averages and set up visualization
years = []
grades = []

for year in data_dict:
    # calculate average grade and save to data_dict
    data_dict[year] = sum(data_dict[year])/len(data_dict[year])
    # append values to separate lists in order to visualize
    years.append(year)
    grades.append(data_dict[year])

plt.plot(years, grades)


if __name__ == "__main__":
    print(data_dict)
    plt.show()
