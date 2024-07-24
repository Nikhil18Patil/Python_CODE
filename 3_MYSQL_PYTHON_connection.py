import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nikhil@18"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nikhil@18",
            database="school"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database_and_table():
    connection = connect_to_mysql()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS school")
        cursor.execute("USE school")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                age INT,
                grade FLOAT
            )
        """)
        connection.commit()
    except Error as e:
        print(f"Error creating database/table: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_student(first_name, last_name, age, grade):
    connection = connect_to_database()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, age, grade)
        cursor.execute(sql, values)
        connection.commit()
    except Error as e:
        print(f"Error inserting student: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_student_grade(first_name, new_grade):
    connection = connect_to_database()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        sql = "UPDATE students SET grade = %s WHERE first_name = %s"
        values = (new_grade, first_name)
        cursor.execute(sql, values)
        connection.commit()
    except Error as e:
        print(f"Error updating student grade: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_student(last_name):
    connection = connect_to_database()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        sql = "DELETE FROM students WHERE last_name = %s"
        values = (last_name,)
        cursor.execute(sql, values)
        connection.commit()
    except Error as e:
        print(f"Error deleting student: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()

def fetch_all_students():
    connection = connect_to_database()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"Error fetching students: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    create_database_and_table()
    insert_student("Alice", "Smith", 18, 95.5)
    fetch_all_students()
    update_student_grade("Alice", 97.0)
    fetch_all_students()
    delete_student("Smith")
    fetch_all_students()

if __name__ == "__main__":
    main()
