# Importing modules
import os
import csv

# Creating csv path reference
csv_path = os.path.join('employee_data.csv')

# Opening and reading csv
with open(csv_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file,delimiter=',')

    # Skipping over header row
    csv_header = next(csvreader)

    # Initializing global variables
    emp_lst = []
    employee = []
    emp_id = ''
    first = ''
    last = ''
    dob = ''
    ssn = ''
    state = ''
    new_header = []
    
    # Initializing dictionary to reference state abbreviations
    state_abv = {
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

    # Iterate through each row of csv
    for row in csvreader:
        # Breaking apart old column definitions by row value
        emp_id = row[0]
        first = row[1].split(' ')[0]
        last = row[1].split(' ')[1]
        dob = row[2].split('-')[1] + '/' + row[2].split('-')[2] + '/' + row[2].split('-')[0]
        ssn = '***-**-' + row[3].split('-')[2]
        state = state_abv[row[4]]

        # Rebuilding rows with new column definitions
        employee.append(emp_id)
        employee.append(first)
        employee.append(last)
        employee.append(dob)
        employee.append(ssn)
        employee.append(state)

        # Converting rows from lists to comma separated strings in a new list
        emp_lst.append(','.join(employee))

        # Resetting each row
        employee = []

    # Writing a new csv in the correct format
    with open('employee_cleaned.csv', 'w', newline='') as file:
        writer =csv.writer(file)
        writer.writerow(['Emp ID,First Name,Last Name,DOB,SSN,State'])
        for employee in emp_lst:
            writer.writerow([employee])
