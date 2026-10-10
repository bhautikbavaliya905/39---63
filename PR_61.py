import MySQLdb

# Connect to MySQL
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS dbStudent")

# Select database
cursor.execute("USE dbStudent")

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tblStudInfo (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(50),
    stream VARCHAR(50),
    college_name VARCHAR(100),
    contact_number VARCHAR(15),
    remarks VARCHAR(100)
)
""")

# Input student information
name = input("Enter student name: ")
stream = input("Enter stream: ")
college = input("Enter college name: ")
contact = input("Enter contact number: ")
remarks = input("Enter remarks: ")

# Insert data
sql = """
INSERT INTO tblStudInfo
(student_name, stream, college_name, contact_number, remarks)
VALUES (%s, %s, %s, %s, %s)
"""

value = (name, stream, college, contact, remarks)

cursor.execute(sql, value)

db.commit()

print("Student information inserted successfully.")

db.close()

