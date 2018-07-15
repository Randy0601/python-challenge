# import modules
import os
import csv

# Set path for file
# or use csvpath = os.path.join('..', 'Resources', 'election_data.csv') if not using direct link
csvpath = r"C:/Users/randy/Documents/Data Analytics/Homework/Week 3/python-challenge/Resources/budget_data.csv"

# Open csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip first title row
    csv_header = next(csvreader)
    revenue = []
    monthcount = []
    rev_change = []

     # Count total months and sum revenue 
    for row in csvreader:
        revenue.append(int(row[1]))
        monthcount.append(row[0])
        # total_months = len(monthcount)

       # Calculate difference between all row of column revenue and found total revnue change, then divide by count of months for the average.
       # Finding the max and min change with corresponding month. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1]) 
        total_change = sum(rev_change)  
        avg_rev_change = sum(rev_change)/(len(monthcount)-1)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_change_date = str(monthcount[rev_change.index(max(rev_change))+1])
        min_change_date = str(monthcount[rev_change.index(min(rev_change))+1])

# Create printout as output to use to print in terminal and create text file.
Output = (
    f'\nFinancial Analysis\n'
    f'-----------------------------------\n'
    f'Total Months: {len(monthcount)}\n'
    f'Total Revenue: ${sum(revenue)}\n'
    f'Avereage Change: ${round(avg_rev_change, 2)}\n'
    f'Greatest Increase in Revenue: {max_change_date} ${max_rev_change}\n'
    f'Greatest Decrease in Revenue: {min_change_date} ${min_rev_change}\n')

print(Output)

# Create a text file and print result
with open('PyBank.txt', 'w') as txt_file:
    txt_file.write(Output)


#     print("Financial Analysis", file = f)
#     print("----------------------------------", file = f)
#     print("Total Months:", len(monthcount), file = f)
#     print("Total Revenue: $",sum(revenue), file = f)
#     print("Avereage Change: $",round(avg_rev_change, 2), file = f)
#     print("Greatest Increase in Revenue:", max_change_date,"($",max_rev_change,")", file = f)
#     print("Greatest Decrease in Revenue:", min_change_date,"($",min_rev_change,")", file = f)