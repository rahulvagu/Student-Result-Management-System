from flask import Flask, render_template, request
from db_config import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    student_id = request.form['student_id']

    # Connect to DB
    conn = get_connection()
    cursor = conn.cursor()

    # Fetch student info
    cursor.execute("SELECT name, department FROM Students WHERE student_id = %s", (student_id,))
    student = cursor.fetchone()

    # Fetch subject-wise marks
    cursor.execute("""
        SELECT Subjects.name, Marks.marks
        FROM Marks
        JOIN Subjects ON Marks.subject_id = Subjects.subject_id
        WHERE Marks.student_id = %s
    """, (student_id,))
    marks = cursor.fetchall()

    # Debug prints in terminal
    print("Student ID:", student_id)
    print("Student:", student)
    print("Marks:", marks)

    conn.close()

    return render_template('result.html', student=student, marks=marks)

if __name__ == '__main__':
    app.run(debug=True)
