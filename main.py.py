import datetime

patients_list = [
    {
        "Name": "Siva",
        "Gender": "Male",
        "Age": 45,
        "Condition": "Arrhythmias",
        "Treatment": "Medications"
    },
    {
        "Name": "Jenny",
        "Gender": "Female",
        "Age": 28,
        "Condition": "Kidney stones",
        "Treatment": "Medications"
    },
]

doctors_list = [
    {
        "Name": "Dr. Jason",
        "Speciality": "Cardiology"
    },
    {
        "Name": "Dr. Jasper",
        "Speciality": "Urologist"
    },
]

nurses_list = [
    {
        "Name": "Katte",
        "Speciality": "Cardiology",
    },
    {
        "Name": "Cindy",
        "Speciality": "Urologist",
    },
]

appointments = [
    {
        "Patient_Name": 'Halim',
        "Doctor": 'Dr. Jasper',
        "Date_Time": '2024-07-19 15:00'
    },
    {
        "Patient_Name": 'Tan',
        "Doctor": 'Dr. Jason',
        "Date_Time": '2024-07-18 10:00'
    }
]

billing_records = [
    {
        "Name": "Siva",
        "Amount_Due": 450,
        "Insurance_claim_status": "Approved"
    },
    {
        "Name": "Jenny",
        "Amount_Due": 1000,
        "Insurance_claim_status": "Pending"
    },
]

#user login details: admin, dcotor, nurse & patient
def login():
    user_name = input("Username: ").lower()
    password = input("Password: ")

    if user_name == "admin" and password == "admin123":
        return "admin"
    elif user_name == "doctor" and password == "doctor123":
        return "doctor"
    elif user_name == "nurse" and password == "nurse123":
        return "nurse"
    elif user_name == "patient" and password == "patient123":
        return "patient"
    else:
        print("Invalid username or password")
        return None

#main menu for all user
def main_menu():
    print(" " + "-" * 28)
    print(f"|\t\t Menu: \t\t\t\t|")
    print(" " + "-" * 28)
    print(f"|\t 1.Login \t\t\t\t|")
    print(f"|\t 2.Exit Application \t|")
    print(" " + "-" * 28)

#main menu for admin with all function
def main_menu_login_admin():
    while True:
        print(" " + "-" * 32)
        print(f"|\t\t Menu: \t\t\t\t\t|")
        print(" " + "-" * 32)
        print(f"|\t a.Manage Users \t\t\t|")
        print(f"|\t b.Reporting and Analytics \t|")
        print(f"|\t c.Billing Management\t\t|")
        print(f"|\t d.Appointment Management\t|")
        print(f"|\t e.Patients Details \t\t|")
        print(f"|\t f.Exit to Main Menu \t\t|")
        print(" " + "-" * 32)

        choice2 = input("Enter your choice: ").lower()
        if choice2 == "a":
            main_menu_login_manage_user_admin()
        elif choice2 == "b":
            generateReport()
        elif choice2 == "c":
            viewBill()
        elif choice2 == "d":
            manageAppointment()
        elif choice2 == "e":
            viewPatient()
        elif choice2 == "f":
            return

        else:
            print("Invalid option")

#main menu for admin to add, view & delete user
def main_menu_login_manage_user_admin():
    while True:
        print(" " + "-" * 36)
        print(f"|\t\t Menu: \t\t\t\t\t\t|")
        print(" " + "-" * 36)
        print(f"|\t a.Add Users \t\t\t\t\t|")
        print(f"|\t b.Delete Users \t\t\t\t|")
        print(f"|\t c.View Users \t\t\t\t\t|")
        print(f"|\t d.Exit to Previous Main Menu\t|")
        print(" " + "-" * 36)

        choice3 = input("Enter your choice: ").lower()
        if choice3 == "a":
            addUsers()
        elif choice3 == "b":
            deleteUser()
        elif choice3 == "c":
            viewUser()
        elif choice3 == "d":
            return

        else:
            print("Invalid option")

#main menu for doctor without billing management, doctor only can view appointments list
#add patient detail's in part b
def main_menu_login_doctor():
    while True:
        print(" " + "-" * 32)
        print(f"|\t\t Menu: \t\t\t\t\t|")
        print(" " + "-" * 32)
        print(f"|\t a.Manage Users \t\t\t|")
        print(f"|\t b.Reporting and Analytics \t|")
        print(f"|\t c.Appointment Management\t|")
        print(f"|\t d.Patients Details \t\t|")
        print(f"|\t e.Exit to Main Menu \t\t|")
        print(" " + "-" * 32)

        choice4 = input("Enter your choice: ").lower()
        if choice4 == "a":
            main_menu_login_manage_user_doctor()
        elif choice4 == "b":
            to_generate_or_add_report = input("Please type 'generate' to generate patient report, 'add' to add new patient's details: ").lower()
            if to_generate_or_add_report == "generate":
                generateReport()
            elif to_generate_or_add_report == "add":
                add_patient_report()
            else:
                print("Invalid option")
        elif choice4 == "c":
            manageAppointment_doctor()
        elif choice4 == "d":
            viewPatient()
        elif choice4 == "e":
            return

        else:
            print("Invalid option")

#doctor only can view user
def main_menu_login_manage_user_doctor():
    while True:
        print(" " + "-" * 36)
        print(f"|\t\t Menu: \t\t\t\t\t\t|")
        print(" " + "-" * 36)
        print(f"|\t a.View Users \t\t\t\t\t|")
        print(f"|\t b.Exit to Previous Main Menu\t|")
        print(" " + "-" * 36)

        choice5 = input("Enter your choice: ").lower()
        if choice5 == "a":
            viewUser()
        elif choice5 == "b":
            return

        else:
            print("Invalid option")

#main menu for nurse without billing management
def main_menu_login_nurse():
    while True:
        print(" " + "-" * 32)
        print(f"|\t\t Menu: \t\t\t\t\t|")
        print(" " + "-" * 32)
        print(f"|\t a.Manage Users \t\t\t|")
        print(f"|\t b.Reporting and Analytics \t|")
        print(f"|\t c.Appointment Management\t|")
        print(f"|\t d.Patients Details \t\t|")
        print(f"|\t e.Exit to Main Menu \t\t|")
        print(" " + "-" * 32)

        choice6 = input("Enter your choice: ").lower()
        if choice6 == "a":
            main_menu_login_manage_user_nurse()
        elif choice6 == "b":
            generateReport()
        elif choice6 == "c":
            manageAppointment()
        elif choice6 == "d":
            viewPatient()
        elif choice6 == "e":
            return

        else:
            print("Invalid option")

#main menu for nurse to add, view & delete user
def main_menu_login_manage_user_nurse():
    while True:
        print(" " + "-" * 36)
        print(f"|\t\t Menu: \t\t\t\t\t\t|")
        print(" " + "-" * 36)
        print(f"|\t a.Add Users \t\t\t\t\t|")
        print(f"|\t b.Delete Users \t\t\t\t|")
        print(f"|\t c.View Users \t\t\t\t\t|")
        print(f"|\t d.Exit to Previous Main Menu\t|")
        print(" " + "-" * 36)

        choice7 = input("Enter your choice: ").lower()
        if choice7 == "a":
            addUsers()
        elif choice7 == "b":
            deleteUser()
        elif choice7 == "c":
            viewUser()
        elif choice7 == "d":
            return

        else:
            print("Invalid option")

#main menu for patient, only for view billing details & appointment management
def main_menu_login_patient():
    while True:
        print(" " + "-" * 32)
        print(f"|\t\t Menu: \t\t\t\t\t|")
        print(" " + "-" * 32)
        print(f"|\t a.Billing Management\t\t|")
        print(f"|\t b.Appointment Management\t|")
        print(f"|\t c.Exit to Main Menu \t\t|")
        print(" " + "-" * 32)

        choice8 = input("Enter your choice: ").lower()
        if choice8 == "a":
            viewBill_patient()
        elif choice8 == "b":
            manageAppointment()
        elif choice8 == "c":
            return

        else:
            print("Invalid option")

#for admin & nurse to add doctors, nurses & patients(without treatment & condition)
def addUsers():
    Add_user = input("Which user you want to add? Doctor, nurse or patient: ").lower()
    if Add_user == "patient":
        while True:
            Name = input("What is the patient's name: ").capitalize()
            if Name.isalpha():
                while True:
                    Gender = input("What is the patient's gender, male/female: ").capitalize()
                    if Gender in ["Male", "Female"]:
                        while True:
                            Age = input("What is the patient's age: ")
                            if Age.isnumeric():
                                Condition = input("What is the patient's condition: ").capitalize()
                                Treatment = input("What is the patient's treatment: ").capitalize()
                                break
                            else:
                                print("Invalid age input, please enter numbers only.")
                        break
                    else:
                        print("Invalid gender input, please enter male of female only.")
                break
            else:
                print("Invalid name, please enter patient's name in alphabets only.")

        def addPatients(patient_name, patient_gender, patient_age):
            newPatient = {}
            newPatient["Name"] = patient_name
            newPatient["Gender"] = patient_gender
            newPatient["Age"] = patient_age
            patients_list.append(newPatient)

        addPatients(Name, Gender, Age)
        print(f"Patient {Name} added.")

    elif Add_user == "doctor":
        while True:
            Name = input("What is the doctor's name: ").capitalize()
            if Name.isalpha():
                DrName = "Dr. " + Name
                while True:
                    Speciality = input("What is the doctor's speciality: ").capitalize()
                    if Speciality.isalpha():
                        break
                    else:
                        print("Invalid speciality input")
                break
            else:
                print("Invalid name, please enter doctor's name in alphabets only.")

        def addDoctors(doctor_name, doctor_speciality):
            newDoctor = {}
            newDoctor["Name"] = doctor_name
            newDoctor["Speicality"] = doctor_speciality
            doctors_list.append(newDoctor)

        addDoctors(DrName, Speciality)
        print(f"{DrName} added.")

    elif Add_user == "nurse":
        while True:
            Name = input("What is the nurse's name: ").capitalize()
            if Name.isalpha():
                while True:
                    Speciality = input("What is the nurse's speciality: ").capitalize()
                    if Speciality.isalpha():
                        break
                    else:
                        print("Invalid speciality input")
                break
            else:
                print("Invalid name, please enter the nurse's name in alphabets only.")

        def addNurses(nurse_name, nurse_speciality):
            newNurse = {}
            newNurse["Name"] = nurse_name
            newNurse["Speicality"] = nurse_speciality
            nurses_list.append(newNurse)

        addNurses(Name, Speciality)
        print(f"Nurse {Name} added.")

    else:
        print("Invalid option")

#delete doctors, nurses & patients
def deleteUser():
    Delete_user = input("Which user you want to delete? Doctor, nurse or patient: ").lower()
    if Delete_user == "patient":
        name = input("Enter the patient's name to delete: ").capitalize()
        global patients_list
        new_patients_list = [patient for patient in patients_list if patient["Name"] != name]
        if len(new_patients_list) < len(patients_list):
            print(f"Patient {name} deleted.")
            patients_list = new_patients_list
        else:
            print("Patient not found")

    elif Delete_user == "doctor":
        name = "Dr. " + input("Enter the doctor's name to delete: ").capitalize()
        global doctors_list
        new_doctors_list = [doctor for doctor in doctors_list if doctor["Name"] != name]
        if len(new_doctors_list) < len(doctors_list):
            print(f"{name} deleted.")
            doctors_list = new_doctors_list
        else:
            print("Doctor not found")

    elif Delete_user == "nurse":
        name = input("Enter the nurse's name to delete: ").capitalize()
        global nurses_list
        new_nurses_list = [nurse for nurse in nurses_list if nurse["Name"] != name]
        if len(new_nurses_list) < len(nurses_list):
            print(f"Nurse {name} deleted.")
            nurses_list = new_nurses_list
        else:
            print("Nurse not found")
    else:
        print("Invalid option")

# view doctors, nurses & patients
def viewUser():
    View_user = input("Which category of user you want to view? Doctor, nurse or patient: ").lower()
    if View_user == "patient":
        for patientslist in patients_list:
            patients_details = {key: patientslist[key] for key in ["Name", "Gender", "Age"]}
            print(patients_details)

    elif View_user == "doctor":
        for doctorslist in doctors_list:
            print(doctorslist)

    elif View_user == "nurse":
        for nurseslist in nurses_list:
            print(nurseslist)

    else:
        print("Invalid option")

#manage appointment- only admin, nurse & patient can access
def manageAppointment():
    appointment_choice = input(
        "Please type 'add' to add appointment, 'view' to view appointment, 'reschedule' to reschedule appointment, 'cancel' to cancel appoitnment: ").lower()
    if appointment_choice == "add":
        while True:
            Patient_Name = input("Please enter your the patient's name to add appointment: ").capitalize()
            if Patient_Name.isalpha():
                for doctorslist in doctors_list:
                    print(doctorslist)
                while True:
                    Doctor = input(
                        "Above are the doctors and their specialities currently available, please enter the doctor you will you like to consult: ").capitalize()
                    if Doctor.isalpha():
                        DoctorName = "Dr. " + Doctor
                        doctor_name_match = False
                        index = 0
                        while index < len(doctors_list):
                            if DoctorName == doctors_list[index]["Name"]:
                                doctor_name_match = True
                                break
                            index += 1
                        if doctor_name_match:
                            while True:
                                Date_Time = input(
                                    "Please enter the date and time for appointment, [eg: 2024-06-17 14:00] :")
                                try:
                                    datetime_checker = datetime.datetime.strptime(Date_Time, "%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print(
                                        "Invalid date and time format. Please enter a valid date and time (YYYY-MM-DD HH:MM).")
                            break
                        else:
                            print("Doctor's name not found")
                            for doctorslist in doctors_list:
                                print(doctorslist)
                    else:
                        print("Invalid doctor's name only.")
                break
            else:
                print("Invalid name, please enter the patient's name alphabets only.")

        def add_appointment(patient_name, doctor_name, date_time):
            new_appointment = {}
            new_appointment["Patient_Name"] = patient_name
            new_appointment["Doctor"] = doctor_name
            new_appointment["Date_Time"] = date_time
            appointments.append(new_appointment)

        add_appointment(Patient_Name, DoctorName, Date_Time)
        print(f"Appointment with {DoctorName} added.")

    elif appointment_choice == "view":
        for appointment in appointments:
            print(appointment)

    elif appointment_choice == "reschedule":
        patient_name_to_change_date_time = input(
            "Please enter the patient's name to reschedule appointment: ").capitalize()
        for appointment in appointments:
            if appointment["Patient_Name"] == patient_name_to_change_date_time:
                while True:
                    new_date_time = input(
                        f"Please enter the new date and time for {patient_name_to_change_date_time}'s appointment, [eg: 2024-06-17 14:00] :")
                    try:
                        datetime_checker = datetime.datetime.strptime(new_date_time, "%Y-%m-%d %H:%M")
                        appointment["Date_Time"] = new_date_time
                        print(f"{patient_name_to_change_date_time}'s appointment has been updated.")
                        break
                    except ValueError:
                        print(
                            "Invalid date and time format. Please enter a valid date and time (YYYY-MM-DD HH:MM).")
                break
        if appointment["Patient_Name"] != patient_name_to_change_date_time:
            print(f"{patient_name_to_change_date_time}'s appointment record not found")

    elif appointment_choice == "cancel":
        patient_name_to_cancel = input("Please enter the patient's name to cancel appointment: ").capitalize()
        for i, appointment in enumerate(appointments):
            if appointment["Patient_Name"] == patient_name_to_cancel:
                del appointments[i]
                print(f"{patient_name_to_cancel}'s appointment has been cancelled")
                break
        else:
            print(f"{patient_name_to_cancel}'s appointment not found.")

    else:
        print("Invalid option")

#for doctor to view appointments list
def manageAppointment_doctor():
    print("Below are the list of appointments found.")
    for appointment in appointments:
            print(appointment)

#to generate paitent's report
def generateReport():
    view_or_search = input(
        "Enter 'view' to view the patient's report and 'search' for searching specific condition: ").lower()
    if view_or_search == "view":
        patient_name_to_view = input("Enter patient name to view the patient's report: ").capitalize()

        def view_Patient_Report(patient_name):
            for patient in patients_list:
                if patient["Name"] == patient_name_to_view:
                    return patient
            return "Patient not found."

        print(view_Patient_Report(patient_name_to_view))

    elif view_or_search == "search":
        condition_to_view = input("Enter the condition to search for: ").capitalize()

        def search_condition(condition):
            for patient in patients_list:
                if patient["Condition"] == condition_to_view:
                    return patient
            return "No patients found with this condition."

        print(search_condition(condition_to_view))

    else:
        print("Invalid option")

#for doctor only to add patient's details
def add_patient_report():
    while True:
        Name = input("What is the patient's name: ").capitalize()
        if Name.isalpha():
            while True:
                Gender = input("What is the patient's gender, male/female: ").capitalize()
                if Gender in ["Male", "Female"]:
                    while True:
                        Age = input("What is the patient's age: ")
                        if Age.isnumeric():
                            Condition = input("What is the patient's condition: ").capitalize()
                            Treatment = input("What is the patient's treatment: ").capitalize()
                            break
                        else:
                            print("Invalid age input, please enter numbers only.")
                    break
                else:
                    print("Invalid gender input, please enter male of female only.")
            break
        else:
            print("Invalid name, please enter patient's name in alphabets only.")

    def addPatients(patient_name, patient_gender, patient_age, patient_condition, patient_treatment):
        newPatient = {}
        newPatient["Name"] = patient_name
        newPatient["Gender"] = patient_gender
        newPatient["Age"] = patient_age
        newPatient["Condition"] = patient_condition
        newPatient["Treatment"] = patient_treatment
        patients_list.append(newPatient)

    addPatients(Name, Gender, Age, Condition, Treatment)
    print(f"Patient {Name}'s details added.")

# only admin can access this function to view, search & change status of insurance claim
def viewBill():
    billing_options = input(
        "Enter 'view' to view all the patient's billing report, 'search' for searching specific patient's billing report and 'insurance' to manage the patient's insurance claim: ").lower()
    if billing_options == "view":
        for records in billing_records:
            print(records)

    elif billing_options == "search":
        patient_name_to_search = input("Enter the patient's name to search for his/her billing records: ").capitalize()

        def search_billing_records(patient_name):
            for records in billing_records:
                if records["Name"] == patient_name_to_search:
                    return records
            return "Billing record not found."

        print(search_billing_records(patient_name_to_search))

    elif billing_options == "insurance":
        patient_name_to_update_insurance = input(
            "Enter the patient's name to update for his/her insurance claim status: ").capitalize()
        claim_status = input("Enter the patient's insurance status: ").capitalize()

        def manage_insurance_claim(record_name, claim_status):
            for records in billing_records:
                if records["Name"] == patient_name_to_update_insurance:
                    records["Insurance_claim_status"] = claim_status
                    return "Claim status updated."
            return "Billing record not found."

        print(manage_insurance_claim(patient_name_to_update_insurance, claim_status))

# for patient to change his/her billing details
def viewBill_patient():
    patient_name_to_search = input("Enter the patient's name to search for his/her billing records: ").capitalize()

    def search_billing_records(patient_name):
        for records in billing_records:
            if records["Name"] == patient_name_to_search:
                return records
        return "Billing record not found."

    print(search_billing_records(patient_name_to_search))

#for admin, doctor & nurse to check all the patients list
def viewPatient():
    for patientlists in patients_list:
        print(patientlists)

def exit():
    print("Exit successfully, goodbye!")

while True:
    main_menu()
    choice1 = input("Enter your choice: ")
    if choice1 == "1":
        user_role = login()

        if user_role == "admin":
            main_menu_login_admin()

        elif user_role == "doctor":
            main_menu_login_doctor()

        elif user_role == "nurse":
            main_menu_login_nurse()

        elif user_role == "patient":
            main_menu_login_patient()

    elif choice1 == "2":
        exit()
        break

    else:
        print("Invalid option")

