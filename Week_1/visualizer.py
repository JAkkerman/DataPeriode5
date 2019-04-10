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
GRAPH_TITLE = "Average grading per year of release of movies in IMDB top 50"
START_YEAR = 2008
END_YEAR = 2018

def get_grades(infile):
    """
    Calculates the average grades for movies in release year
    """
    # Global dictionary for the data
    data_dict = {str(key): [] for key in range(START_YEAR, END_YEAR)}

    # for all the rows that are not the header, add grades to release years
    with open(infile, newline='') as moviesfile:
        moviesreader = csv.reader(moviesfile)
        for row in moviesreader:
            if row[2].isdigit():
                data_dict[row[2]].append(float(row[1]))

    # calculate averages and set up visualization
    years = []
    grades = []

    for year in data_dict:
        # calculate average grade and save to data_dict
        data_dict[year] = sum(data_dict[year])/len(data_dict[year])
        # append values to separate lists in order to visualize
        years.append(year)
        grades.append(data_dict[year])

    return years, grades


def visualize(title, years, grades):
    """
    Visualizes the given data
    """

    plt.plot(years, grades)
    plt.title(title)
    plt.ylabel("Grade")
    plt.xlabel("Year")
    plt.ylim([0, 10])
    plt.show()


if __name__ == "__main__":
    # extract grades and years from the csv file
    years, grades = get_grades(INPUT_CSV)

    # plot the line diagram of averages
    visualize(GRAPH_TITLE, years, grades)
