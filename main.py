
while True:
    file_name = input("Please enter file name: ")

    if file_name.split('.')[-1] == 'csv':
        break

    else:
        print("Error: not a csv file")


print("Reading information from " + file_name)
