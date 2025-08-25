import mysql.connector

def get_connection():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass",
    database="fastapi_raw_queries"
)