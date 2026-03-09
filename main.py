import mysql.connector
from mysql.connector import Error
import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


# Add a student record


def add_student(connection):
    cursor = connection.cursor()
    print("\n--- Add Student Record ---")
    name = input("Enter Student Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    class_name = input("Enter Class: ")
    section = input("Enter Section: ")
    gender = input("Enter Gender (Male/Female/Other): ")
    father_name = input("Enter Father Name: ")
    mother_name = input("Enter Mother Name: ")
    contact_number = input("Enter Contact Number: ")
    address = input("Enter Address: ")
    registration_date = datetime.date.today().strftime("%Y-%m-%d")

    query = """
        INSERT INTO students (name, dob, class, section, gender, father_name, mother_name, contact_number, address, registration_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        name,
        dob,
        class_name,
        section,
        gender,
        father_name,
        mother_name,
        contact_number,
        address,
        registration_date,
    )

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Student record added successfully!")
    except Error as e:
        print(f"Error adding record: {e}")


# Display all student records
def display_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        print("\nStudent Records:")

        for record in records:
            print(record)
    except Error as e:
        print(f"Error fetching students: {e}")


# Search for a student record by name
def search_student(connection):
    cursor = connection.cursor()
    name = input("Enter Student Name to Search: ")

    query = "SELECT * FROM students WHERE name = %s"
    cursor.execute(query, (name,))
    record = cursor.fetchone()

    if record:
        print("\n--- Record Found ---")

        print(f"Student Record: {record}")
    else:
        print("No record found with that name.")


# Update a student record by ID
def update_student(connection):
    cursor = connection.cursor()
    student_id = input("Enter Student ID to Update: ")
    column = input("Enter the field to update (e.g., name, dob, class, address): ")
    new_value = input(f"Enter the new value for {column}: ")

    query = f"UPDATE students SET {column} = %s WHERE id = %s"
    try:
        cursor.execute(query, (new_value, student_id))
        connection.commit()
        print("Record updated successfully!")
    except Error as e:
        print(f"Error updating record: {e}")


# Delete a student record by ID
def delete_student(connection):
    cursor = connection.cursor()
    student_id = input("Enter Student ID to Delete: ")

    query = "DELETE FROM students WHERE id = %s"
    try:
        cursor.execute(query, (student_id,))
        connection.commit()
        print("Record deleted successfully!")
    except Error as e:
        print(f"Error deleting record: {e}")


# Submit Fee for a student


def submit_fee(connection):

    print("Registration Fees for Class Nur to 12th")
    print("\n1.Nursery to UKG : ₹1000")
    print("2. Primary (Grades 1 to 5): ₹2,500")
    print("3. Secondary (Grades 6 to 10): ₹3,500")
    print("4. Higher Secondary (Grades 11 and 12): ₹4,500")

    cursor = connection.cursor()
    print("\n--- Submit Fee ---")

    student_id = input("Enter Student ID to Submit Fee: ")
    registration_fee = input("Enter Registration Fee: ")

    # Validate fee input
    try:
        registration_fee = float(registration_fee)
    except ValueError:
        print("Invalid input for registration fee. Please enter a numeric value.")
        return

    fee_date = datetime.date.today().strftime("%Y-%m-%d")
    status = "Paid"

    # Insert fee record into fee_records table

    query = """
        INSERT INTO fee_records (student_id, registration_fee, fee_date, status)
        VALUES (%s, %s, %s, %s)
    """
    values = (student_id, registration_fee, fee_date, status)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Fee submitted successfully!")
    except Error as e:
        print(f"Error submitting fee: {e}")


# Display all fee records


def display_fee_records(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM fee_records")
        records = cursor.fetchall()

        print("\nFee Records:")

        for record in records:
            print(record)
    except Error as e:
        print(f"Error fetching fee records: {e}")


# Main Menu


def main():
    connection = create_connection()
    if not connection:

        print("Failed to connect to the database. Exiting...")
        return

    while True:
        print("\n--- School Record System ---")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student Record")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Submit Fee for Student")
        print("7. Display All Fee Records")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(connection)
        elif choice == "2":
            display_students(connection)
        elif choice == "3":
            search_student(connection)
        elif choice == "4":
            update_student(connection)
        elif choice == "5":
            delete_student(connection)
        elif choice == "6":
            submit_fee(connection)
        elif choice == "7":
            display_fee_records(connection)
        elif choice == "8":
            connection.close()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program

if __name__ == "__main__":
    main()
