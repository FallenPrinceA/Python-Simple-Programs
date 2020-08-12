# Purpose: To hold the data about employees and creat three Employee objects to
    # hold that data.

class Employee:
    # Initialize the employee with their name, ID, department, and job title.
    def __init__(self, name, ID, department, job_title):
        self.__name = name
        self.__ID = ID
        self.__dept = department
        self.__job = job_title

    # Change the department of the employee
    def set_department(self, department):
        self.__dept = department

    # Change the job title of the employee
    def set__job_title(self, job_title):
        self.__job = job_title

    # Get the employee's name
    def get_name(self):
        return self.__name

    # Get the employee's ID number
    def get_ID_number(self):
        return self.__ID

    # Get the employee's department
    def get_department(self):
        return self.__dept

    # Get the employee's job title
    def get_job_title(self):
        return self.__job

    # Get all current information about the meployee in printable form
    def __str__(self):
        return 'Name: ' + self.__name + '\n' +  \
               'ID Number: ' + str(self.__ID) + '\n' +  \
               'Department: ' + self.__dept + '\n' +  \
               'Job Title: ' + self.__job

# The three Employees
susan = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
mark = Employee('Mark Jones', 39119, 'IT', 'Programmer')
joy = Employee('Joey Rodgers', 81774, 'Manufacturing', 'Engineer')

# Display the information
print(susan, end = '\n\n')
print(mark, end = '\n\n')
print(joy, end = '\n\n')
