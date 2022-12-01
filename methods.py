class Employee:
    def employeeDetails(self):
        self.name = 'Ben'
        self.age = 30
    
    @staticmethod
    def welcomeMessage():
        print("Welcome aboard!!")
employee1 = Employee()
employee1.employeeDetails()
employee1.welcomeMessage()