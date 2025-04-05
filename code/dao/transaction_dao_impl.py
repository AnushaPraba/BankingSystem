from util.db_conn_util import DBConnUtil
from dao.transaction_dao import TransactionDAO

class TransactionDAOImpl(TransactionDAO):
    def transact(self, account_number, tran_type, amount):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO Transactions (account_number, transaction_type, amount)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (account_number, tran_type, amount))
        conn.commit()

        cursor.close()
        conn.close()

    def get_transactions(self, account_number):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT transaction_type, amount, transaction_date
            FROM Transactions
            WHERE account_number = %s
            ORDER BY transaction_date ASC
        """
        cursor.execute(sql, (account_number,))
        transactions = cursor.fetchall()

        cursor.close()
        conn.close()
        return transactions
