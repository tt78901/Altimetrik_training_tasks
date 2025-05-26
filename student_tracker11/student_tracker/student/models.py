from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    department = models.CharField(max_length=50)
    year_of_admission = models.IntegerField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    exam_marks = models.FloatField()
    assignment_marks = models.FloatField()
    attendance_percent = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.course_name}"
