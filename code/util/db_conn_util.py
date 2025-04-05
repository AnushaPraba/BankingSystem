import mysql.connector

class DBConnUtil:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Anu3@mysql",
            database="hmbank"
        )
