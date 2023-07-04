# Function to remind the patient 
def send_reminders(patients):
    # sender_email = 'your_email@example.com'
    # sender_password = 'your_password'
    sender_email = 'your_email@example.com'
    sender_password = 'your_password'
    #sender_password=print("Enter your password, ")
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