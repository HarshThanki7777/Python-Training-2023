import datetime
import os
import uuid

def get_user_details():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    vaccine_name = input("Enter the vaccine name: ")
    vaccine_dose = input("Enter the vaccine dose: ")
    return name, email, age, gender, vaccine_name, vaccine_dose

def write_to_file(filename, details):
    with open(filename, 'w') as file:
        file.write("ID: {}\n".format(details[0]))
        file.write("Name: {}\n".format(details[1]))
        file.write("Email: {}\n".format(details[2]))
        file.write("Age: {}\n".format(details[3]))
        file.write("Gender: {}\n".format(details[4]))
        file.write("Vaccine Name: {}\n".format(details[5]))
        file.write("Vaccine Dose: {}\n".format(details[6]))
        file.write("Date and Time: {}\n\n".format(datetime.datetime.now()))

def main():
    if not os.path.exists("patients"):
        os.makedirs("patients")

    patient_id = uuid.uuid4().int
    filename = os.path.join("patients", f"{patient_id}.txt")
    
    details = (patient_id,) + get_user_details()
    write_to_file(filename, details)
    print("Details written to {}.".format(filename))

if __name__ == "__main__":
    main()
