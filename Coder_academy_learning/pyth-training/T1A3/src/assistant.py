import csv
# Constants for file paths
CSV_FILE_PATH = 'clinic.csv'


# Function to load patient data from a CSV file
def load_patients(filename):
    patients = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients.append(row)
    return patients

# Function to save patient data to a CSV file 
def save_patients(filename, patients):
    fieldnames = ['name', 'contact_number', 'email', 'appointment_date']
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)

# Function for booking an appointment
def book_appointment(patients):
    # Gather patient information
    name = input("Enter patient's name: ")
    contact_number = input("Enter patient's contact number: ")
    email = input("Enter patient's email address (optional): ")
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")

    # Create a patient dictionary
    patient = {
        'name': name,
        'contact_number': contact_number,
        'email': email,
        'appointment_date': appointment_date
    }

    # Add the patient to the list and save to file
    patients.append(patient)
    save_patients(CSV_FILE_PATH, patients)
    print("Appointment booked successfully!")

# Function for canceling an appointment
def delete_appointment(patients):
    # Get the name of the patient to delete
    name = input("Enter patient's name to delete the appointment: ")
    removed = False
    for patient in patients:
        if patient['name'] == name:
            patients.remove(patient)
            removed = True
            save_patients(CSV_FILE_PATH, patients)
            print("Appointment deleted successfully!")
            break
    if not removed:
        print("Appointment not found!")


# Function to display the menu options
def display_menu():
    print("Clinic Appointment Booking and Reminder")
    print("1. Book Appointment")
    print("2. Delete Appointment")
    print("3. Quit")
    