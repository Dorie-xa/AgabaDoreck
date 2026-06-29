import csv
import json
import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "students.csv")
JSON_FILE = os.path.join(BASE_DIR, "students.json")
LOG_FILE = os.path.join(BASE_DIR, "student_system.log")

#logging configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#exception
class StudentNotFoundError(Exception):
    pass
#create files
def initialize_files():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["RegNo", "Name", "Age", "Gender"])

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as file:
            json.dump({}, file)

def load_json():
    with open(JSON_FILE, "r") as file:
        return json.load(file)
    
def save_json(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

#add student 
def add_student():
    try:
        reg = input("Registration Number: ").strip()
        name = input("Student Name: ").strip()
        age = int(input("Age: "))
        gender = input("Gender: ").strip()
        address = input("Address: ").strip()
        contact = input("Contact: ").strip()
        program = input("Program: ").strip()

        # Check duplicate registration number
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row[0] == reg:
                    print("Student already exists.")
                    return
        
                   # Save CSV
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([reg, name, age, gender])

        # Save JSON
        data = load_json()
        data[reg] = {
            "address": address,
            "contact": contact,
            "program": program
        }

        save_json(data)

        logging.info(f"Added student {reg}")
        print("Student added successfully.")

    except ValueError:
        logging.error("Invalid age entered.")
        print("Age must be a number.")

    except Exception as e:
        logging.error(str(e))
        print("An error occurred.")

    finally:
        print("Operation Completed.\n")

# View Students

def view_students():
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)
            data = load_json()
            print("\n==============================")

            for row in reader:
                reg = row[0]
                print(f"Registration : {reg}")
                print(f"Name         : {row[1]}")
                print(f"Age          : {row[2]}")
                print(f"Gender       : {row[3]}")

                if reg in data:
                    print("Address      :", data[reg]["address"])
                    print("Contact      :", data[reg]["contact"])
                    print("Program      :", data[reg]["program"])
                print("----------------------------")

    except Exception as e:
        logging.error(str(e))
        print("Unable to display students.")

# Search Student
def search_student():
    try:
        reg = input("Enter Registration Number: ")
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)
            found = False
            data = load_json()

            for row in reader:
                if row[0] == reg:
                    found = True
                    print("\nStudent Found")
                    print("Registration :", row[0])
                    print("Name :", row[1])
                    print("Age :", row[2])
                    print("Gender :", row[3])

                    if reg in data:
                        print("Address :", data[reg]["address"])
                        print("Contact :", data[reg]["contact"])
                        print("Program :", data[reg]["program"])

            if not found:
                raise StudentNotFoundError("Student not found.")

    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)

    finally:
        print("Search Complete.\n")

# Update Student
def update_student():

    try:
        reg = input("Registration Number: ")
        rows = []
        found = False

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if row[0] == reg:
                    found = True
                    row[1] = input("New Name: ")
                    row[2] = input("New Age: ")
                    row[3] = input("New Gender: ")
                rows.append(row)

        if not found:
            raise StudentNotFoundError("Student not found.")

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        data = load_json()

        data[reg]["address"] = input("New Address: ")
        data[reg]["contact"] = input("New Contact: ")
        data[reg]["program"] = input("New Program: ")
        save_json(data)

        logging.info(f"Updated student {reg}")
        print("Record Updated.")

    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)

    finally:
        print("Update Complete.\n")

# Delete Student
def delete_student():
    try:
        reg = input("Registration Number: ")
        rows = []
        found = False

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if row[0] == reg:
                    found = True
                    continue
                rows.append(row)

        if not found:
            raise StudentNotFoundError("Student not found.")

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        data = load_json()

        if reg in data:
            del data[reg]
        save_json(data)

        logging.info(f"Deleted student {reg}")
        print("Student deleted.")

    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)

    finally:
        print("Delete Complete.\n")

# Main Menu
initialize_files()
while True:
    print("\n========= STUDENT RECORD MANAGEMENT =========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        logging.info("Program exited.")
        print("Thank you.")

        break
    else:
        print("Invalid Choice.")