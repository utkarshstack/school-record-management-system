# User Manual

School Record Management System

This manual explains how to use the School Record Management System.

---

## Starting the Program

Run the program:

```
python main.py
```

The system will display a menu with available options.

---

## Menu Options

### 1. Add Student Record

This option allows the administrator to register a new student.

Information required:

* Student Name
* Date of Birth
* Class
* Section
* Gender
* Father Name
* Mother Name
* Contact Number
* Address

The system automatically stores the registration date.

---

### 2. Display All Records

Displays all students stored in the database along with their details.

---

### 3. Search Student Record

Allows searching for a student by entering the student's name.

If the student exists, the system will display their information.

---

### 4. Update Student Record

Allows modification of an existing student record.

Steps:

1. Enter the student ID
2. Enter the field you want to update
3. Enter the new value

Example fields:

* name
* dob
* class
* address

---

### 5. Delete Student Record

Deletes a student record from the database.

Steps:

1. Enter the student ID
2. Confirm deletion

---

### 6. Submit Fee for Student

Allows recording registration fee payments.

Fee structure example:

Nursery – UKG → ₹1000
Primary (1–5) → ₹2500
Secondary (6–10) → ₹3500
Higher Secondary (11–12) → ₹4500

Steps:

1. Enter student ID
2. Enter fee amount
3. Fee will be stored with date and status "Paid"

---

### 7. Display All Fee Records

Shows all recorded fee transactions for students.

---

### 8. Exit

Closes the program safely.

---

## Important Notes

* Ensure MySQL server is running before starting the program.
* The database `school_db` must exist.
* Tables `students` and `fee_records` must be created beforehand.
* The `.env` file must contain correct database credentials.

---

## Troubleshooting

**Database connection error**

Check:

* MySQL server is running
* Username and password are correct
* Database exists

**Module not found error**

Run:

```
pip install -r requirements.txt
```

---

## End of Manual
