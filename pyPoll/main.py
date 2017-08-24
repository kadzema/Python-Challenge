# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os, csv
candidates = []
uniqueCandidates = []
# totalVotes = 0
results = {}
candidateVotes = 0

rawPath = os.path.join("raw_data")
rawFile = "election_data_2.csv"
inputFile = os.path.join(rawPath,rawFile)
outputFile = rawFile.replace(".csv","_output.txt")

with open(inputFile) as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        # append all Candidate votes to a list
        candidates.append(row["Candidate"])
        # totalVotes += 1
# length of list = count of votes
totalVotes = len(candidates)
# create a list of unique candidates
uniqueCandidates = set(candidates)

# write the results to a file
with open(outputFile,"w") as textFile:
    textFile.write("Election Results\n")
    textFile.write("---------------------------\n")
    textFile.write("Total Votes: " + str(totalVotes) + "\n")
    textFile.write("---------------------------\n")

    # loop through unique candidate list
    for c in uniqueCandidates:
        # write candidate name and percentage of votes for candidate followed by candidate vote count
        textFile.write(c + ": " + '{:.0%}'.format(candidates.count(c)/totalVotes) + " (" + str(candidates.count(c)) + ")\n")
        #create a dictionary, use candidate as key and count as value
        results[c] = candidates.count(c)

    textFile.write("---------------------------\n")

    # loop through results and get winner (candidate with highest number of votes) - does not handle ties
    for key, value in results.items():
        if value > candidateVotes:
            candidateVotes = value
            winner = key

    textFile.write("Winner: " + winner + "\n")
    textFile.write("---------------------------\n")

# print results file to screen
with open(outputFile,'r') as readOutput:
    print(readOutput.read())



 




