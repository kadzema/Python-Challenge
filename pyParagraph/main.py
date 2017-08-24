# Assess the passage for each of the following:
# Approximate word count
# Approximate sentence count
# Approximate letter count (per word)
# Average sentence length (in words)

import os, csv, re

rawPath = os.path.join("raw_data")
rawFile = "paragraph_2.txt"
fullFile = os.path.join(rawPath,rawFile)
analysisFile = rawFile.replace(".txt","_Analysis.txt")
letterCount = 0

# read in the passage
with open(fullFile, 'r') as inputFile:
    paragraph = inputFile.read()

# split on spaces to get words into a list
words = paragraph.split(" ")
# loop through the words in word list and count len of each to get total letter count
for w in words:
    letterCount = letterCount + len(w)
# length of word list = count of words
wordCount = len(words)
# divide letter count by word count to get average number of letters per word
avgLetters = letterCount/wordCount 

# split where . ? or ! possibly followed by " followed by a space"
sentences = re.split(r'[\.\?\!][\"]?[\s]',paragraph)
# length of sentence list = count of sentences
sentenceCount = len(sentences)
# divide word count by sentence count to get average number of words per sentence
avgWords = wordCount/sentenceCount

# write the results to a file
with open(analysisFile,'w') as outputFile:
    outputFile.write("Paragraph Analysis\n")
    outputFile.write("--------------------------\n")
    outputFile.write("Approximate Word Count: " + str(wordCount) + "\n")
    outputFile.write("Approximate Sentence Count: " + str(sentenceCount) + "\n")
    outputFile.write("Average Letter Count: " + str(avgLetters) + "\n")
    outputFile.write("Average Sentence Length: " + str(avgWords) + "\n")

# print the output file to the screen
with open(analysisFile,'r') as readOutput:
    print(readOutput.read())

