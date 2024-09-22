import pyodbc
from pymongo import MongoClient

def connect_to_database_sql():
    # Chuỗi kết nối SQL Server
    server = 'htthlxoto.database.windows.net'
    database = 'htthlxoto'
    username = 'database'
    password = '28072002Vu@'
    # driver= '{ODBC Driver 17 for SQL Server}'
    driver= 'FreeTDS'
    # Tạo chuỗi kết nối
    connection_string = f'DRIVER={{{driver}}};SERVER={server};PORT=1433;UID={username};PWD={password};DATABASE={database};TDS_Version=7.4;Encrypt=yes;TrustServerCertificate=no;'
   
    # Tạo chuỗi kết nối
    # connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    # Kết nối đến cơ sở dữ liệu
    conn = pyodbc.connect(connection_string)
    return conn

# test kết nối
def test_connect_to_database_sql():
    try:
        conn = connect_to_database_sql()
        print("Connected to SQL Server")
        return True
    except Exception as e:
        print(e)
        return False

test_connect_to_database_sql()
# lấy thông tin bảng users
def get_data(query):
    try:
        conn = connect_to_database_sql()
        cursor = conn.cursor()

        # Thực hiện truy vấn
        cursor.execute(query)

        # Lấy tất cả dữ liệu
        rows = cursor.fetchall()

        # In ra từng bản ghi
        for row in rows:
            print(row)

        # Đóng kết nối
        cursor.close()
        conn.close()
    except Exception as e:
        print("Đã xảy ra lỗi:", e)

# Gọi hàm để lấy thông tin từ bảng users
get_data("SELECT * FROM users; ")
get_data("SELECT * FROM users WHERE rfid_id = 'SV001';")


