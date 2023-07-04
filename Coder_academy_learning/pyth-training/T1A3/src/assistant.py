import csv
import datetime
import smtplib
from email.mime.text import MIMEText
# Constants for file paths
CSV_FILE_PATH = 'clinic.csv'




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
    # I wrped those sentences to repeat until user put correct date
    while True:
        appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
        try:
            #appointment_date = datetime.datetime.strptime(appointment_date, '%Y-%m-%d').date()
            datetime.datetime.strptime(appointment_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
            continue
        # Check if the appointment date is within the available days
        available_dates = view_available_days(patients)
        appointment_date = datetime.datetime.strptime(appointment_date, '%Y-%m-%d').date()
        if appointment_date not in available_dates:
            print("Please choose another day. This day is not available.")
            #here we can give the user to choose continue or go to menu again 
            choice = input("Do you want to try again? (Y/N): ")
            while choice.lower() not in ['y', 'n']:
                print("Please choose 'Y' for Yes or 'N' for No.")
                choice = input("Do you want to try again? (Y/N): ")
            if choice.lower() == 'n':
                return
            #return
            # here we can skip because the day is not available 
            continue
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
        break    


# Function to remind the patient 
def send_reminders(patients):
    # sender_email = 'your_email@example.com'
    # sender_password = 'your_password'
    sender_email = 'your_email@example.com'
    sender_password = 'your_password'
    today = datetime.date.today()
    # here you can use suitable rminder after 2, 3, or 4 days from current day
    reminder_date = today + datetime.timedelta(days=3)  # Calculate the reminder date
    for patient in patients:
        appointment_date = datetime.datetime.strptime(str(patient['appointment_date']), '%Y-%m-%d').date()
        if appointment_date == reminder_date:
        #if appointment_date == today:
            subject = f"Appointment Reminder: {patient['name']}"
            message = f"Dear {patient['name']},\n\nThis is a reminder for your appointment {reminder_date}. Please arrive on time.\n\nBest regards,\nYour Name"

            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = patient['email']

            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    #server.sendmail(sender_email, "example0@gmail.com", msg.as_string("Hello again"))
                    server.sendmail(sender_email, patient['email'], msg.as_string())
                print(f"Reminder sent to {patient['name']}!")
            except Exception as e:
                print(f"Error occurred while sending reminder to {patient['name']}: {str(e)}")



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


