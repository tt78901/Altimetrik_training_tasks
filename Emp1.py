class Employee1:
    company_name="Southern Infotech Pvt Ltd"
    def __init__(self,name,emp_id,department,salary):
        self.name=name
        self.emp_id=emp_id
        self.department=department
        self.salary=salary
        
    def display_details(self):
        print(f"Company   : {Employee1.company_name}")
        print(f"Name       : {self.name}")
        print(f"Emp ID     : {self.emp_id}")
        print(f"Salary     : {self.salary}")
        print("_" * 30)

    def annual_salary(self):
        return self.salary * 12
    
    def apply_increment(self,percentage):
        increment=self.salary * (percentage / 100)
        self.salary +=increment

    def is_high_earner(self):
        return self.salary > 70000
    
    @staticmethod
    def welcome_message():
        print("Welcome to Southern Infotech Pvt LTd")

emp1=Employee1("Tarun","EMP101","HR",50000)
emp2=Employee1("Mohan", "EMP102","IT",100000)
emp1.annual_salary()
emp2.annual_salary()


emp1.apply_increment(10)
emp1.display_details()
emp2.display_details()

print(f"Is {emp2.name} a high earner? : {'yes'if emp2.is_high_earner() else 'No'}")
Employee1.welcome_message()



