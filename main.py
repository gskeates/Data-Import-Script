import csv, getpass, mysql.connector
from mysql.connector import Error

def get_file_name():
    while True:
        file_name = input("Please enter file name: ")

        if file_name.split('.')[-1] == 'csv':
            return file_name

        else:
            print("Error: not a csv file")


file_name = get_file_name()

# Open file
with open(file_name, "r") as f:
    reader = csv.reader(f)
    columns = next(reader)
    file_rows = list(reader)


# Establish database connection
username = input("Please enter your database username: ")
pwd = getpass.getpass(prompt="Please enter the database password: ", stream=None)
database = input("Please enter the database name: ")

try:
    connection = mysql.connector.connect(host='localhost',
                                         database=database,
                                         user=username,
                                         password=pwd)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

# Insert data into table
table_name = file_name.split('.')[0]


create_table_statement = ""


cursor.execute("CREATE TABLE %s", data)
