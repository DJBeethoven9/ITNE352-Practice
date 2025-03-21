#importing the csv file data
import csv

#loading the data from the csv file
def load_data(file):
    with open(file, 'r') as employee_file:
        reader = csv.DictReader(employee_file)
        data = [row for row in reader]
    return data

#saving the data to the csv file
def save_data(file, data):
    with open(file, 'a', newline='') as employee_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
        if employee_file.tell() == 0:
            writer.writeheader()
        writer.writerow(data[-1])

#displaying the menu
def display_menu():
    print("\n==================== Menu ====================")
    print("1. Search for record by ID")
    print("2. Show total records")
    print("3. Display all records")
    print("4. Add a new record")
    print("0. Exit")
    print("==============================================")

#searching the record by ID
def search_by_id(data, emp_id):
    for row in data:
        if row['ID'] == emp_id:
            print("")
            print(f"Employee Name: {row['Employee Name']}, Position: {row['Position Title']}, Experience: {row['Experience']} Years")
            return
    print("Employee not found.")

#showing the total records
def show_total_records(data):
    print("")
    print(f">> Total number of records: {len(data)} <<")

#displaying all the records
def display_all_records(data):
    for row in data:
        print(f"{row['Employee Name']} ({row['Gender']}): {row['Position Title']} ({row['Performance in 2025']}%)")

#adding a new record to the csv file
def add_record(file, data):
    while True:
        new_id = input("Enter ID: ")
        if any(row['ID'] == new_id for row in data):
            print("\nID already has been used. Please enter another ID.")
        else:
            break

    new_record = {}
    new_record['ID'] = new_id
    new_record['Employee Name'] = input("Enter Employee Name: ")
    
#checking the Gender input and validating it
    while True:
        gender = input("Enter Gender: ").lower()
        if gender in ['male', 'm']: #it will convert the input to lowercase
            new_record['Gender'] = 'Male'
            break
        elif gender in ['female', 'f']: #it will convert the input to lowercase
            new_record['Gender'] = 'Female'
            break
        else: #if the input is not valid, it will print the message
            print("Invalid gender input. Please enter 'male', 'm', 'female', or 'f'.")

#checking the Position Title input and validating it
    new_record['Position Title'] = input("Enter Position Title: ")
    
#checking the Experience input and validating it
    while True:
        try:
            experience = int(input("Enter Experience: "))
            if experience < 0:
                raise ValueError("Experience cannot be negative.")
            new_record['Experience'] = experience
            break
        except ValueError as e:
            print(f"Try again!")

#checking the Performance in 2025 input and validating it
    while True:
        try:
            performance = int(input("Enter Performance in 2025 (0-100): "))
            if performance < 0 or performance > 100:
                raise ValueError("Performance must be between 0 and 100.")
            new_record['Performance in 2025'] = performance
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a number between 0 and 100.")
    data.append(new_record)
    save_data(file, data)
    print("Record added successfully.")

#defining the main function & if there is no need to call the function, it will not be called 
def main():
    file = 'Employee_data.csv'
    data = load_data(file)
    
    while True:
        display_menu()
        number_key = input("Enter a Number: ")
        
        if number_key == '1':
            emp_id = input("Enter Employee ID: ")
            search_by_id(data, emp_id)
        elif number_key == '2':
            show_total_records(data)
        elif number_key == '3':
            display_all_records(data)
        elif number_key == '4':
            add_record(file, data)
        elif number_key == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
            

#calling the main function
if __name__ == "__main__":
    main()


