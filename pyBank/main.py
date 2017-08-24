# 1. The total number of months included in the dataset
# 2. The total amount of revenue gained over the entire period
# 3. The average change in revenue between months over the entire period
# 4. The greatest increase in revenue (date and amount) over the entire period
# 5. The greatest decrease in revenue (date and amount) over the entire period
# 6. Print to terminal and write results to text file

import os, csv, sys
dates = []
revenues = []
highest = 0 
lowest = 0

rawPath = os.path.join("raw_data")
# change this to user input?
rawFile = "budget_data_1.csv"

fullFile = os.path.join(rawPath,rawFile)
# check that the file exists
# how to do this?
fileOut = rawFile.replace(".csv","_output.txt")

#open the raw input file for reading
with open(fullFile,'r',newline = '') as readFile:
    csvreader = csv.reader(readFile,delimiter=",")
    #skip the header row
    next(csvreader) 
    for row in csvreader:
        #put the dates into a list
        dates.append(row[0])
        #put the revenues into a list
        revenues.append(int(row[1]))
        # check for highest revenue
        if(int(row[1]) > highest) or highest == 0:
            highest = int(row[1])
            highestIndex = len(revenues)
        # check for lowest revenue
        if(float(row[1]) < lowest) or lowest == 0:
            lowest = int(row[1])
            lowestIndex = len(revenues)

# count the list items - gets number of months
totalMonths = len(dates)
# sum the list items - gets the total revenue
totalRevenues = sum(revenues)

# write the results to a file
writeFile = open(fileOut,'w')
writeFile.write("Financial Analysis\n")
writeFile.write("------------------------------------\n")
writeFile.write("Total Months: " + str(totalMonths) + "\n")
writeFile.write("Total Revenue: " + str('${:,.2f}'.format(totalRevenues)) + "\n")
#divide total revenue by number of months - gets average change in revenue
writeFile.write("Average Revenue Change: " + str('${:,.2f}'.format(totalRevenues/totalMonths)) + "\n")
writeFile.write("Greatest Increase in Revenue: " + dates[highestIndex-1] + "  (" + str('${:,.2f}'.format(revenues[highestIndex-1])) + ")\n")
writeFile.write("Greatest Decrease in Revenue: " +  dates[lowestIndex-1] + "  (" + str('${:,.2f}'.format(revenues[lowestIndex-1])) + ")\n")
writeFile.close()

# print the results file to the screen
with open(fileOut,'r') as readOutput:
    print( readOutput.read()) 





