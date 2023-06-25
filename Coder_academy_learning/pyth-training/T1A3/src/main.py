#print("hello world")
import csv




# Constants for file paths
CSV_FILE_PATH = 'clinic.csv'
# function to load file 
def load_patients(filename):
    patients = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients.append(row)
    return patients

# function to save file depend on pationts 
def save_patients(filename, patients):
    fieldnames = ['name', 'contact_number', 'email', 'appointment_date']
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)

# booking function
def book_appointment(patients):
    name = input("Enter patient's name: ")
    contact_number = input("Enter patient's contact number: ")
    email = input("Enter patient's email address (optional): ")
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")

    patient = {
        'name': name,
        'contact_number': contact_number,
        'email': email,
        'appointment_date': appointment_date
    }
    patients.append(patient)
    save_patients(CSV_FILE_PATH, patients)
    print("Appointment booked successfully!")

# function to cancle the appointment
def delete_appointment(patients):
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


# display menue to choose task
def display_menu():
    print("Clinic Appointment Booking and Reminder")
    print("1. Book Appointment")
    print("2. Delete Appointment")
    print("3. Qui")
    
# main file to run the functions 
def main():
    patients = load_patients(CSV_FILE_PATH)

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            book_appointment(patients)
        elif choice == '2':
            delete_appointment(patients)
        elif choice == '3':
            save_patients(CSV_FILE_PATH, patients)
            print("Exiting Clinic Appointment Booking and Reminder. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()