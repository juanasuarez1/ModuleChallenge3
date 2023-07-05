# Import modules
import os
import csv

#create file path for given csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Set variables equal to 0 to start for loop, open parantheses for strings
total_months = 0
total_value = 0
total_change = 0
change = 0
change_freq = 0
pre_profit = 0
greatest_increase = 0
greatest_increase_month = ''
greatest_decrease = 0
greatest_decrease_month = ''

# Open file with CSV reader
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read the header row
    csv_header = next(csvreader)

    for row in csvreader:
        
        #Use for loop to count each row as a month
        total_months += 1

        #Get value of first row and iterate over adding each one
        total_value += int(row[1])

        # Set current profit to the first line and it will chage as we iterate
        current_profit = int(row[1])

        # We include this as 1st row has nothing before it so there is no change, this function skips that first row
        if pre_profit != 0:
            change = current_profit - pre_profit
            total_change += change
            change_freq += 1

        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0]


        pre_profit = current_profit




output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_value}
Average Change: ${total_change/change_freq:.2f}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""

print(output)

