from Conn import Conn


try:
    conn = Conn()
    conn.db_connect()
    print('ok')
except Exception as error:
    print(error)