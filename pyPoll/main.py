# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------

#assume one vote per id
#should confirm this - best way to do this?

#open file and read as dictionary
#can ignore county

#length of dictionary is count of votes
#create a dictionary with key = candidate and ids as list of values?
#or - write each candidate/vote to a list?
import os, csv
candidates = []
uniqueCandidates = []
totalVotes = 0
results = {}
candidateVotes = 0

path = os.path.join("..","..","Instructions","PyPoll","raw_data")
inputFile = os.path.join(path,"election_data_2.csv")
outputFile = inputFile.replace(".csv","_output.txt")
with open(inputFile) as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        candidates.append(row["Candidate"])
        totalVotes += 1
uniqueCandidates = set(candidates)

with open(outputFile,"w") as textFile:
    textFile.write("Election Results\n")
    textFile.write("---------------------------\n")
    textFile.write("Total Votes: " + str(totalVotes) + "\n")
    textFile.write("---------------------------\n")

    for c in uniqueCandidates:
        # print(c + " " + '{:.0%}'.format(candidates.count(c)/totalVotes) + " (" + str(candidates.count(c)) + ")")
        textFile.write(c + ": " + '{:.0%}'.format(candidates.count(c)/totalVotes) + " (" + str(candidates.count(c)) + ")\n")
        #create a dictionary, use candidate as key and count as value
        results[c] = candidates.count(c)

    textFile.write("---------------------------\n")

    # print(results)
    for key, value in results.items():
        if value > candidateVotes:
            candidateVotes = value
            winner = key

    # print("Winner: " + winner)
    textFile.write("Winner: " + winner + "\n")
    textFile.write("---------------------------\n")

with open(outputFile,'r') as readOutput:
    print(readOutput.read())



 




