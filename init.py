class Employee:
    def __init__(self,name):
        self.name = name
    def showEmployeeName(self):
        print("Name :",self.name)

emp1 = Employee('Ben')
emp1.showEmployeeName()