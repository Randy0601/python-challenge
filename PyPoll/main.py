# import modules
import os
import csv

# Set path for file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Open csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip first title row
# Create list, dictionary and counter
    csv_header = next(csvreader)
    total_votes = 0
    candidate = ""
    candidate_votes = {}
    candidate_percentages ={}
    winner_votes = 0
    winner = ""

    # Count votes
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# calculate vote percentage and identify winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.3%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

# print results to terminal
print("Election Results")
print("----------------------------------")
print("Total Votes: ", total_votes)
print("----------------------------------")
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print("----------------------------------")
print(f"Winner: {winner}")
print("----------------------------------")

# Create text file with same print results.
with open('PyPoll.txt', 'w') as f:
    print("Election Results", file = f)
    print("----------------------------------", file = f)
    print("Total Votes: ", total_votes, file = f)
    print("----------------------------------", file = f)
    for person, vote_count in candidate_votes.items():
        print(f"{person}: {candidate_percentages[person]} ({vote_count})", file = f)
    print("----------------------------------", file = f)
    print(f"Winner: {winner}", file = f)
    print("----------------------------------", file = f)



