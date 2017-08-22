# Assess the passage for each of the following:

# Approximate word count

# Approximate sentence count

# Approximate letter count (per word)

# Average sentence length (in words)

# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.56557377049
# Average Sentence Length: 24.4

import os, csv

path = os.path.join("..","..","Instructions","pyParagraph","raw_data")
fullFile = os.path.join(path,"paragraph_2.txt")
analysisFile = fullFile.replace(".txt","_Analysis.txt")
letterCount = 0

with open(fullFile, 'r') as inputFile:
    paragraph = inputFile.read()

words = paragraph.split(" ")
for w in words:
    letterCount = letterCount + len(w)
wordCount = len(words)
avgLetters = letterCount/wordCount 
sentences = paragraph.split(".")
sentenceCount = len(sentences) -1 #since it's the last character in the string? best practice? check if any element = ""?
avgWords = wordCount/sentenceCount


with open(analysisFile,'w') as outputFile:
    outputFile.write("Paragraph Analysis\n")
    outputFile.write("--------------------------\n")
    outputFile.write("Approximate Word Count: " + str(wordCount) + "\n")
    outputFile.write("Approximate Sentence Count: " + str(sentenceCount) + "\n")
    outputFile.write("Average Letter Count: " + str(avgLetters) + "\n")
    outputFile.write("Average Sentence Length: " + str(avgWords) + "\n")

with open(analysisFile,'r') as readOutput:
    print(readOutput.read())

