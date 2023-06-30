import csv
import datetime
# Function to load patient data from a CSV file
def load_patients(filename):
    patients = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            #row['appointment_date'] = datetime.datetime.strptime(row['appointment_date'], '%Y-%m-%d').date()
            patients.append(row)
    return patients