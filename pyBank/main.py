# 1. The total number of months included in the dataset

# 2. The total amount of revenue gained over the entire period

# 3. The average change in revenue between months over the entire period

# 4. The greatest increase in revenue (date and amount) over the entire period

# 5. The greatest decrease in revenue (date and amount) over the entire period

# 6. Print to terminal and write results to text file

#get the name of the file to read
#sample data
# Date,Revenue
# Oct-12,1154293
# need to check for duplicates?
# ok to sort data first and re-save?

#open the file for reading
#put the date into a list, count the list items - gets number of months
#put the revenues into a list and sum the list items - gets the total revenue
#divide total revenue by number of months - gets average change in revenue
#loop through the rows and get the highest revenue 
#loop through the rows in data and get the lowest revenue

import os, csv, sys
dates = []
revenues = []
highest = 0 #try setting this to the first revenue in the file
lowest = 0 #try setting this to the first revenue in the file

path = os.path.join("..","..","Instructions","PyBank","raw_data")
outputPath = os.path.join("..","..","Instructions","PyBank")
# print("select a file from the following path",path)
# print(os.listdir(path))
# userFile = input("file: ")
# fullFile = os.path.join(path,userFile)
fullFile = os.path.join(path,"budget_data_2.csv")
fileOut = fullFile.replace(".csv","_output.txt")
with open(fullFile,'r',newline = '') as readFile:
    csvreader = csv.reader(readFile,delimiter=",")
    #skip the header row
    next(csvreader) # could prompt user to ask to do this'
    for row in csvreader:
        dates.append(row[0])
        revenues.append(int(row[1]))
        if(int(row[1]) > int(highest)): #why did i need to make highest an int? set to 0 to start!
            highest = row[1]
            highestIndex = len(revenues)
            # print(highestIndex)
        if(float(row[1]) < int(lowest)):
            lowest = row[1]
            lowestIndex = len(revenues)

writeFile = open(fileOut,'w')
totalMonths = len(dates)
totalRevenues = sum(revenues)

writeFile.write("Financial Analysis\n")
writeFile.write("------------------------------------\n")
writeFile.write("Total Months: " + str(totalMonths) + "\n")
writeFile.write("Total Revenue: " + str('${:,.2f}'.format(totalRevenues)) + "\n")
writeFile.write("Average Revenue Change: " + str('${:,.2f}'.format(totalRevenues/totalMonths)) + "\n")
writeFile.write("Greatest Increase in Revenue: " + dates[highestIndex-1] + "  (" + str('${:,.2f}'.format(revenues[highestIndex-1])) + ")\n")
writeFile.write("Greatest Decrease in Revenue: " +  dates[lowestIndex-1] + "  (" + str('${:,.2f}'.format(revenues[lowestIndex-1])) + ")\n")
writeFile.close()
print(fileOut)
with open(fileOut,'r') as readOutput:
    # lines = readOutput.read()
    # print(lines)
    print( readOutput.read())  #why doesn't this print out?
#print(revenues)
# print(dates[highestIndex])




