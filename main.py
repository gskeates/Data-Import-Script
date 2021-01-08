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
file_rows = list()


# Try to open file
try:
    file = open(file_name)

    file_reader = csv.reader(file)
    for row in file_reader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
        file_rows.append(row)
except Error as e:
    print("Error while opening CSV file ", e)


# Establish database connection
pwd = input("Please enter the database password: ")
'''
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)


'''
