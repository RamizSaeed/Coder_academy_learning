import csv
#import datetime
# Importing the csv module to work with CSV files

# Function definition for load_patients, which takes a filename as input CSV file
def load_patients(filename):
    # Initializing an empty list to store the patient records
    patients = []
    with open(filename, 'r') as file:
        # Opening the specified CSV file in read mode
        reader = csv.DictReader(file)
        # Creating a csv.DictReader object to read the contents of the file as a dictionary
        for row in reader:
            patients.append(row)
            #row['appointment_date'] = datetime.datetime.strptime(row['appointment_date'], '%Y-%m-%d').date()
    return patients
    # Returning the list of patient records after reading and processing the CSV file





