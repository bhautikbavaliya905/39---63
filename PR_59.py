import MySQLdb

# Connect to database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="ksc"
)

cursor = db.cursor()

# Update row
sql = "UPDATE student SET age = %s WHERE name = %s"
value = (21, "Sujal")

cursor.execute(sql, value)

db.commit()

print("Row updated successfully.")

db.close()

