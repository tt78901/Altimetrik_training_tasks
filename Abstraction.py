class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return f"{self.name}  scored {self.marks} marks"
    
    def __len__(self):
        return len(self.name)
    
    def __add__(self,other):
        return self.marks + other.marks
    
s1=student("Anirudh",85)
s2=student("Keerthi",90)

print(s1)
print(len(s1))
print(s1 + s2)