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
student_id = input("Enter student ID to delete: ")

# Delete student information
sql = "DELETE FROM student_info WHERE student_id = %s"
value = (student_id,)

cursor.execute(sql, value)

db.commit()

print("Student information deleted successfully.")

db.close()

