import csv

def filter_employees_by_salary(filename, salary_threshold):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            #print(reader.fieldnames)  # Debug: Print the fieldnames to verify correct reading
            print(f"Employees with salary greater than {salary_threshold}:")
            found = False
            for row in reader:
                try:
                    if float(row['salary']) > salary_threshold:
                        print(f"{row['ename']} - {row['salary']}")
                        found = True
                except ValueError:
                    print(f"Warning: Invalid salary value '{row['salary']}' for employee '{row['ename']}'")

            if not found:
                 print("No employees found above the specified salary.") 
    except FileNotFoundError: 
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    try:
        threshold = float(input("Enter the salary to filter employees: "))
        filter_employees_by_salary('employees.csv', threshold)
    except ValueError:
        print("Error: Please enter a valid number for the salary.")
