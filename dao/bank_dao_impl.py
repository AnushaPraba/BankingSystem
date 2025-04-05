from util.db_conn_util import DBConnUtil
from dao.bank_dao import BankDAO

class BankDAOImpl(BankDAO):

    def find_customer_by_phone_or_email(self, phone, email):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            query = "SELECT customer_id FROM customers WHERE phone_number = %s OR email = %s"
            cursor.execute(query, (phone, email))
            result = cursor.fetchone()
            return result[0] if result else None

        except Exception as e:
            print(f"Error occurred :{e}")
            return None

        finally:
            cursor.close()
            conn.close()

    def insert_customer(self, first_name, last_name, dob, email, phone, address):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO customers (first_name, last_name, dob, email, phone_number, address) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (first_name, last_name, dob, email, phone, address))
        conn.commit()
        customer_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return customer_id

    def get_next_account_number(self):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT MAX(account_number) FROM accounts"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return max(1001, result[0] + 1 if result[0] is not None else 1001)


    def insert_account(self, account_number, customer_id, account_type, balance):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO accounts (account_number, customer_id, account_type, balance)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (account_number, customer_id, account_type, balance))
        conn.commit()
        cursor.close()
        conn.close()
