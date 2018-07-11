# import modules
import os
import csv

# Set path for file
csvpath = r"C:/Users/randy/Documents/Data Analytics/Homework/Week 3/python-challenge/Resources/budget_data.csv"

# Open csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print("Financial Analysis")
    print("----------------------------------")

# Count rows of data
    csv_header = next(csvreader)
    totalmonths = list(csvreader)
    monthcount = len(totalmonths)
    print("Total Months: " + str(monthcount))
    for row in csvreader:
        print(row[0])