# School Record Management System

A command-line based School Record Management System built using **Python and MySQL**.
This application allows administrators to manage student records and fee submissions efficiently.

---

## Features

* Add new student records
* Display all student records
* Search for students by name
* Update student information
* Delete student records
* Submit registration fees
* Display all fee records

---

## Tech Stack

* Python 3
* MySQL Database
* mysql-connector-python
* python-dotenv

---

## Project Structure

```
school-record-management-system
│
├── main.py
├── requirements.txt
├── README.md
├── USER_MANUAL.md
├── .gitignore
└── .env (not uploaded to GitHub)
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/school-record-management-system.git
cd school-record-management-system
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate virtual environment

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project directory.

Example:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=school_db
```

---

## Database Setup

Create a MySQL database:

```
CREATE DATABASE school_db;
```

Create the `students` table:

```
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    class VARCHAR(10),
    section VARCHAR(10),
    gender VARCHAR(10),
    father_name VARCHAR(100),
    mother_name VARCHAR(100),
    contact_number VARCHAR(15),
    address TEXT,
    registration_date DATE
);
```

Create the `fee_records` table:

```
CREATE TABLE fee_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    registration_fee DECIMAL(10,2),
    fee_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```

---

## Running the Program

Run the application using:

```
python main.py
```

You will see a menu like:

```
--- School Record System ---
1. Add Student Record
2. Display All Records
3. Search Student Record
4. Update Student Record
5. Delete Student Record
6. Submit Fee for Student
7. Display All Fee Records
8. Exit
```

---

## Future Improvements

Possible enhancements:

* Graphical User Interface (GUI)
* Student attendance system
* Fee payment tracking
* Admin authentication
* Web-based version using Flask or Django

---

## Author

Utkarsh Patel

---

## License

This project is open source and available for educational purposes.
