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

path = os.path.join("..","..","Instructions","pyBoss","raw_data")
fullFile = os.path.join(path,"employee_data2.csv")
convertedFile = fullFile.replace(".csv","_converted.csv")
# stateFilePath = os.path.join("..","us_state_abbrev.py")

with open(fullFile,'r') as inputFile, open(convertedFile,'w', newline='') as outputFile:
    columns = ["Emp ID","First Name","Last Name","DOB","SSN","State"]
    writer = csv.writer(outputFile, delimiter= ",")
    writer.writerow(columns)
    reader = csv.DictReader(inputFile, skipinitialspace = True, delimiter = ",")
    #readerOfStates = csv.DictReader(StateFile)
    # stateDic = StateFile.read().replace("us_state_abbrev = ","")
    # stateDic = stateDic.replace("{","").replace("}","")
    # StateAbbrev = stateDic.split(",")
    # StateDic = {}
    # for s in StateAbbrev:
    #     # print(s)
    #     s = s.split(":")
    #     print(s)
        # StateDic[s[0]] = s[1]
    # print(stateDic) 
    # for states in readerOfStates:
    #     print(states.values())
        #reader.next() #do i need to skip the header?
    for row in reader:
        print(row)
        empid = row["Emp ID"]
        fullName = row["Name"].split(" ")
        if row["Name"].count(" ") > 1:
            print(row["Name"])
            firstName = ""
            for x in range(len(fullName)-1):
                firstName = firstName + " " + (fullName[x])
            lastName = fullName[len(fullName)-1]
        else:
            firstName = fullName[0]
            lastName = fullName[1]
            # print(row["DOB"])
        DOB = row["DOB"].split("-")
        DOB = DOB[2]+"/"+DOB[1]+"/" + DOB[0]
        SSN = row["SSN"].split("-")
        SSN = "***-**-" + SSN[2]
        StateAbbrev = us_state_abbrev[row["State"]]
        
        
        line = [empid,firstName,lastName,DOB,SSN, StateAbbrev]
        writer.writerow(line)
        # writer.writerow( ("id",firstName,lastName,"DOB","SSN", "State") )
        # print("id" + firstName+ lastName+"DOB"+"SSN"+ "State")

    

    
