# last row id  --->
import requests
import sqlite3


r = requests.get('https://hackbulgaria.com/api/students/')
# print(r.json())
# print(r.headers)
input_json = r.json()

db_name = 'hackbulgaria_info.db'
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create base for students
query_create_students = '''
    CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    github TEXT)
    '''
cursor.execute(query_create_students)
query_insert_into_students = '''
    INSERT INTO students(name, github)
    VALUES(?, ?)
    '''
for student in input_json:
    # print(student['name'])
    temp_name = student['name']
    temp_github = student['github']
    cursor.execute(query_insert_into_students, (temp_name, temp_github))
    conn.commit()

# Create base for courses
courses_set = set()

query_create_courses = '''
    CREATE TABLE IF NOT EXISTS courses(
    course_id INTEGER PRIMARY KEY,
    course_name TEXT)
    '''
cursor.execute(query_create_courses)
query_insert_into_courses = '''
    INSERT INTO courses(course_name)
    VALUES(?)
    '''
for student in input_json:
    temp_course_name = student['courses']
    cursor.execute(query_insert_into_courses, (temp_course_name,))
    conn.commit()

# Create relation base ( add group here, add primar key(optional))
query = '''
    CREATE TABLE IF NOT EXISTS students_to_courses
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(course_id) REFERENCES couses(couse_id)
    '''
