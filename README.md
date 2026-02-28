# 🎓 Student Result Management System


The Student Result Management System is a Flask and MySQL based web application used to store and process student academic results.
It allows entering subject-wise marks and automatically calculates total, percentage, and grade for each student.
The database is designed using relational tables such as students, subjects, and results to maintain accurate academic records.
This project helped me implement backend logic for real-time result computation and efficient data retrieval.
---
## 🚀 Features

- Add student details
- Enter subject-wise marks
- Automatic total calculation
- Percentage calculation
- Grade generation
- View student results
- Update & delete records
- MySQL database integration
- Responsive user interface

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS, Bootstrap
- Backend: Flask (Python)
- Database: MySQL
- Template Engine: Jinja2

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
### 2️⃣ Create Virtual Environment
    python -m venv venv
## 3️⃣ Install Dependencies
    pip install -r requirements.txt
### 4️⃣ Database Configuration (MySQL)
    Open MySQL and create a database:
    CREATE DATABASE student_result_db;
    Import the provided SQL file into the database.
    Update your MySQL credentials in app.py:
    mysql = MySQL(app)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'your_username'
    app.config['MYSQL_PASSWORD'] = 'your_password'
    app.config['MYSQL_DB'] = 'student_result_db'
### 5️⃣ Run the Application
    python app.py
    Open in browser:
    http://127.0.0.1:5000
```bash
git clone https://github.com/rahulvagu/your-student-result-repo-name.git
cd your-student-result-repo-name
