import MySQLdb

# Connect to MySQL
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()

# Get databases
cursor.execute("SHOW DATABASES")

print("Existing Databases:")

for database in cursor:
    print(database[0])

db.close()

