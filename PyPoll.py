# Add our dependancies.
import os
import csv

# Assign a variable to load a file from a path.
file_to_load = "election_results_Connor.csv"

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a vote counter
total_votes = 0

# Create a list for candidates
candidate_options = []

# Create a dictionary to count votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Count up total amount of votes
        total_votes = total_votes + 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate's name to the candidates list
            candidate_options.append(candidate_name)

            # Begin tracking this candidates vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    ## Determine the percentage of votes for each candidate
    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # print name and number of votes
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

print(winning_candidate_summary)
