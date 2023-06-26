import csv
import datetime
# Constants for file paths
CSV_FILE_PATH = 'clinic.csv'


# Function to load patient data from a CSV file
def load_patients(filename):
    patients = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            #row['appointment_date'] = datetime.datetime.strptime(row['appointment_date'], '%Y-%m-%d').date()
            patients.append(row)
    return patients

# Function to save patient data to a CSV file 
def save_patients(filename, patients):
    fieldnames = ['name', 'contact_number', 'email', 'appointment_date']
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)

# Function to display the available days
def view_available_days(patients):
    # store available days in list
    available_dates = []
    # Get the start and end dates for the week
    today = datetime.date.today()
    next_week_start = today + datetime.timedelta(days=(7 - today.weekday()))
    next_week_end = next_week_start + datetime.timedelta(days=6)
    print("Available Days:")
    # here I use nested loops to iterate in patients list file within period from today to next week end
    current_date = today
    while current_date <= next_week_end:
        has_appointment = False
        for patient in patients:
            appointment_date = datetime.datetime.strptime(str(patient['appointment_date']), '%Y-%m-%d').date()
            if appointment_date == current_date:
                has_appointment = True
                break
        if not has_appointment:
            # here we can add if the day is free from apointment to the available list
            # this will aid us to use it in booking function 
            available_dates.append(current_date)
            print(current_date.strftime("%Y-%m-%d"))
        current_date += datetime.timedelta(days=1)

    return available_dates


# Function for booking an appointment
def book_appointment(patients):
    # Gather patient information
    name = input("Enter patient's name: ")
    contact_number = input("Enter patient's contact number: ")
    email = input("Enter patient's email address (optional): ")
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")

    # Check if the appointment date is within the available days
    available_dates = view_available_days(patients)
    appointment_date = datetime.datetime.strptime(appointment_date, '%Y-%m-%d').date()
    if appointment_date not in available_dates:
        print("Please choose another day. This day is not available.")
        return

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


# Function to remind the patient 
def send_reminder_email(patient):
# this is simulation to send a message to email
    print(f"Reminder: Dear {patient['name']}, your appointment is scheduled on {str(patient['appointment_date'])}. Please make sure to arrive on time.")

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
    print("1. View Available Days")
    print("2. Book Appointment")
    print("3. Delete Appointment")
    print("4. Reminder")
    print("5. Quit")
    