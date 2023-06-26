from assistant import load_patients, save_patients,view_available_days, book_appointment, send_reminder_email, delete_appointment, display_menu
#Define the CSV file path here 
CSV_FILE_PATH = 'clinic.csv' 



#  Main function to run the program
def main():
    
    patients = load_patients(CSV_FILE_PATH)
    #patients = load_patients(CSV_FILE_PATH)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            available_dates = view_available_days(patients)
            if len(available_dates) == 0:
                print("No available dates found.")
        elif choice == '2':
            book_appointment(patients)
        elif choice == '3':
            delete_appointment(patients)
        elif choice == '4':
            # Select a patient from the list
            if len(patients) > 0:
                index = int(input("Enter the index of the patient: "))
                if 0 <= index < len(patients):
                    send_reminder_email(patients[index])
                else:
                    print("Invalid index.")
            else:
                print("No patients found.")  
        elif choice == '5':
            save_patients(CSV_FILE_PATH, patients)
            print("Exiting Clinic Appointment Booking and Reminder. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()