# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #5-1 Class
#  * OOP + Inheritence
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------


class Employee(object):
    ''' Count Total Number of Employees + Display Employee Info (Name + Salary) '''
    num_employees = 0

    # Initialize instances
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employees += 1

    # Display Employee Number
    def employee_num(self):
        print("Employee #", Employee.num_employees)

    # Output Total number of Employees
    def count_employees(self):
        print("Total Number of Employees : %d " % Employee.num_employees)

    # Output Employee's Name and Salary
    def employee_info(self):
        print("Name :", self.name)
        print("Salary : $", self.salary)


class Manager(Employee):
    ''' Inherit Employee Information from Class Employee & Update the total count of employees. '''

    # Initialize and inherit from Class Employee
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)
        self.name = name
        self.salary = salary
        self.totalNum = Employee.num_employees

    # Update the total number of employees
    def get_update_num(self):
        print("Total Number of Employees: ", self.totalNum)

# Invoke members in Class Staff
staff = Employee("Steve", 6000000)
staff.employee_num()
staff.employee_info()
print("-------------------------------------------")
staff.count_employees()
print("")

# Invoke members in Class Manager
manager = Manager("Damon", 1000000)
manager.employee_num()
manager.employee_info()
print("-------------------------------------------")
manager.get_update_num()


