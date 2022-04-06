import mysql.connector

db = mysql.connector.db(
    host = "localhost",
    user = "root",
    password = ""
)

if db.is_connected():
    print("Berhasil terhubung")