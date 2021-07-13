# Assign a variable for the file to load and the path.
import os
import csv

file_to_load = "election_results_Connor.csv"

# Open the election results and read the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print (headers)



# In order to help Tom we need to do the following:

#1. Find the total number of votes cast

#2. Make a complete list of all candidates that recieved votes

#3. Figure out the total amount of votes each candidate won

#4. Calculate the percentage of total votes each candidate won

#5. Determine the winner of the election based on popular votes

