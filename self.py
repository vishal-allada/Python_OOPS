class Employee:
    def employeeDetails(self):
        self.name = "May"
        self.age = 30
    def printEmployeeDetails(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()