from assistant import save_patients,view_available_days, book_appointment, send_reminders, delete_appointment
from load_data import load_patients
from display import display_menu
#Define the CSV file path here 
CSV_FILE_PATH = 'clinic.csv' 
#  Main function to run the program
def main():
    
    patients = load_patients(CSV_FILE_PATH)
    #patients = load_patients(CSV_FILE_PATH)

    while True:
        display_menu()
        # Display the menu options to the user
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            available_dates = view_available_days(patients)
            # Call the view_available_days function to retrieve the available dates
            if len(available_dates) == 0:
                # If there are no available dates, display an appropriate message
                print("No available dates found.")
        elif choice == '2':
            book_appointment(patients)
        elif choice == '3':
            delete_appointment(patients)
        elif choice == '4':
            send_reminders(patients)
        elif choice == '5':
            save_patients(CSV_FILE_PATH, patients)
            print("Exiting Clinic Appointment Booking and Reminder. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()