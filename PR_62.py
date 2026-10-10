import MySQLdb

# Connect to MySQL
db = MySQLdb.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)

cursor = db.cursor()

# Get student ID
student_id = input("Enter student ID: ")

# Get new information
name = input("Enter new student name: ")
stream = input("Enter new stream: ")
college = input("Enter new college name: ")
contact = input("Enter new contact number: ")
remarks = input("Enter new remarks: ")

# Update student information
sql = """
UPDATE student_info
SET student_name = %s,
    stream = %s,
    college_name = %s,
    contact_number = %s,
    remarks = %s
WHERE student_id = %s
"""

value = (name, stream, college, contact, remarks, student_id)

cursor.execute(sql, value)

db.commit()

print("Student information updated successfully.")

db.close()
