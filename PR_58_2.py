import MySQLdb

# Connect to database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="ksc"
)

cursor = db.cursor()

# Insert row
sql = "INSERT INTO student (name, age) VALUES (%s, %s)"
value = ("Sujal", 20)

cursor.execute(sql, value)

db.commit()

print("Row inserted successfully.")

db.close()

