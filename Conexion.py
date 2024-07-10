import mysql.connector

db_connection = mysql.connector.connect(
    user = 'root', 
    password = '', 
    host = 'localhost',
    database = 'gestor_financiero'
)
print(db_connection)