class Employees:
    def __init__(self, ename, salary):
        self.ename = ename
        self.salary = salary

    def __str__(self):
        return f"{self.ename} has a salary of {self.salary}"
    
    def __len__(self):
        return len(self.ename)
    
    def __add__(self, other):
        return self.salary + other.salary

# Create instances outside the class
s1 = Employees("Anirudh", 50000)
s2 = Employees("Arun", 100000)

# Print employee details
print(s1)
print(s2)

# Add salaries
total_salary = s1 + s2
print("Total salary:", total_salary)
