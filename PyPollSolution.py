# Import modules
import os
import csv

#create file path for given csv path
csvpath = os.path.join('Resources', 'election_data.csv')

# Set variables equal to 0 to start for loop
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0
winner = ''

# Open file
with open(csvpath) as csvfile:

    # Establish CSV reader
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Must use since there is a header row
    csv_header = next(csvreader)

    # Start for loop
    for row in csvreader:

        # Count every row as a part of the total
        total_votes += 1

        # We use the next 3 if statements to count the number of votes for each candidate
        if row[2] == "Charles Casper Stockham":

            stockham_votes += 1

        if row[2] == "Diana DeGette":

            degette_votes += 1

        if row[2] == "Raymon Anthony Doane":

            doane_votes += 1
        
        # First 2 if statements give the possibilities of Stockham winning
        if stockham_votes>degette_votes>doane_votes:
            
            winner = "Charles Casper Stockham"

        elif stockham_votes>doane_votes>degette_votes:
            
            winner = "Charles Casper Stockham"

        # Next 2 give the possibility of DeGette winning
        elif degette_votes>stockham_votes>doane_votes:
            
            winner = "Diana DeGette"
        
        elif degette_votes>doane_votes>stockham_votes:
            
            winner = "Diana DeGette"

        # Else covers the other possibility (Doanne winning)
        else:
        
            winner = "Raymon Anthony Doane"


# Output given as f string with our variables
# ':.3f' used to format our answer with 3 decimals
output = (f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {stockham_votes/total_votes*100:.3f}% ({stockham_votes})
Diana DeGette: {degette_votes/total_votes*100:.3f}% ({degette_votes})
Raymon Anthony Doane: {doane_votes/total_votes*100:.3f}% ({doane_votes})
-------------------------
Winner: {winner}
""")

print(output)