import os
import csv

csvpath = os.path.join('..','Employee_Data_Analysis','employee_data_input.csv')

empID = []
firstName = []
lastName = []
dob = []
ssn = []
state = []
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

with open(csvpath,  encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)
    for row in csvreader: 
        # empID 
        empID.append(row[0])
        # split name
        name = row[1].split(" ")
        firstName.append(name[0])
        lastName.append(name[1])
        # format data to MM/DD/YYYY
        splitDate = row[2].split("-")
        formated_date = splitDate[1] + "/" + splitDate[2]+ "/" +splitDate[0]
        dob.append(formated_date)
        # mask SSN
        splitSSN = row[3].split("-")
        maskedSSN = "***-**-" + splitSSN[2]
        ssn.append(maskedSSN)
        state.append(us_state_abbrev[row[4]])

output_csv = zip(empID, firstName, lastName, dob, ssn, state)

csvoutputpath = os.path.join("employee_data_output.csv")

with open (csvoutputpath, 'w', newline='') as datafile: 
    csvwriter = csv.writer(datafile, delimiter=',')
    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    csvwriter.writerows(output_csv)
