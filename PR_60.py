import MySQLdb

# Connect to database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="ksc"
)

cursor = db.cursor()

# Get student ID
id = input("Enter student ID to delete: ")

# Delete student
sql = "DELETE FROM student WHERE id = %s"
value = (id)

cursor.execute(sql, value)

db.commit()

print("Student information deleted successfully.")

db.close()

