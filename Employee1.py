class Employee:

    #constructor
    def __init__(self,empid,empname,salary):
        self.empid=empid
        self.empname=empname
        self.salary=salary
        

    # method to display
    def display(self):
        print(f"Employee ID:{self.empid}")
        print(f"Employee name:{self.empname}")
        print(f"Employee salary:{self.salary}")
        

def main():
    print("Employee Details")
    print("-----------------")
    print("empid\tempname\tsalary")
    
    E1=Employee(111,"Mohan",100000)
    E2=Employee(112,"Ravi",250000)

    E1.display()
    E2.display()

        

if __name__=="__main__":
    main()