# The Name column should be split into separate First Name and Last Name columns.
# The DOB data should be re-written into DD/MM/YYYY format.
# The SSN data should be re-written such that the first five numbers are hidden from view.
# The State data should be re-written as simple two-letter abbreviations.
# 214	Sarah Simpson	12/4/1985	282-01-8166	Florida

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

import os, csv

rawPath = os.path.join("raw_data")
rawFile = "employee_data2.csv"
fullFile = os.path.join(rawPath,rawFile)
convertedFile = rawFile.replace(".csv","_converted.csv")

with open(fullFile,'r') as inputFile, open(convertedFile,'w', newline='') as outputFile:
    columns = ["Emp ID","First Name","Last Name","DOB","SSN","State"]
    writer = csv.writer(outputFile, delimiter= ",")
    writer.writerow(columns)
    reader = csv.DictReader(inputFile, skipinitialspace = True, delimiter = ",")
    for row in reader:
        empid = row["Emp ID"]
        # split full name into first and last
        fullName = row["Name"].split(" ")
        #if there are full names with more than 2 names, put all but last name into first name
        if row["Name"].count(" ") > 1:
            firstName = ""
            for x in range(len(fullName)-1):
                firstName = firstName + " " + (fullName[x])
            lastName = fullName[len(fullName)-1]
        else:
            firstName = fullName[0]
            lastName = fullName[1]
        #  change format of date of birth
        DOB = row["DOB"].split("-")
        DOB = DOB[2]+"/"+DOB[1]+"/" + DOB[0]
        #hide first 5 digits of SSN
        SSN = row["SSN"].split("-")
        SSN = "***-**-" + SSN[2]
        # get state abbreviation
        StateAbbrev = us_state_abbrev[row["State"]]
        
        # put new row into a list
        line = [empid,firstName,lastName,DOB,SSN, StateAbbrev]
        #write list to converted/final file
        writer.writerow(line)
    print(rawFile + " has been converted and saved as " + convertedFile)

    

    
