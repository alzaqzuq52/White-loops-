# Hassan - Week 8 While Loops Assignment
# This program asks for info about up to 5 employees and keeps it organized in a list

# This will hold all employee dictionaries
employees = []

# These are the bad characters we want to block for name, email, and address
bad_name_chars = '!\"@#$%^&*()_=+<>/?;:[]{}\\'
bad_email_chars = '!\"\'#$%^&*()=+<>/?;:[]{}\\'
bad_address_chars = '!\"\'@$%^&*_=+<>?;:[]{}'

# Keep running until we get info for 5 employees
while len(employees) < 5:
    print(f"\nEnter info for employee #{len(employees) + 1}")

    # Ask for ID and keep asking until it's valid
    while True:
        employee_id = input("Enter Employee ID (up to 7 numbers): ")
        if employee_id.isdigit() and len(employee_id) <= 7:
            break
        print("That ID is not valid. Please try again.")

    # Ask for name and check for bad characters
    while True:
        employee_name = input("Enter Employee Name: ")
        if not any(char in bad_name_chars for char in employee_name) and employee_name.replace(" ", "").isalpha():
            break
        print("That name is not valid. Please try again.")

    # Ask for email and make sure it's formatted right
    while True:
        employee_email = input("Enter Employee Email: ")
        if ("@" in employee_email and "." in employee_email and
            not any(char in bad_email_chars for char in employee_email)):
            break
        print("That email is not valid. Please try again.")

    # Ask for address (optional). Only check if something was typed.
    while True:
        employee_address = input("Enter Employee Address (optional): ")
        if employee_address == "":
            break
        elif not any(char in bad_address_chars for char in employee_address):
            break
        print("That address is not valid. Please try again.")

    # Make a dictionary for this employee and store all their info
    employee = {
        'employee_id': employee_id,
        'name': employee_name,
        'email': employee_email,
        'address': employee_address
    }

    # Add the employee to the list
    employees.append(employee)

# After all done, show the full list
print("\nFinal List of Employees:")
for emp in employees:
    print(emp)
