import mysql.connector

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  
)
print(db_connection)