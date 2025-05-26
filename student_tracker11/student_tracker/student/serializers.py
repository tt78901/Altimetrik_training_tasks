from rest_framework import serializers
from .models import Student, Performance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)  # nested
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)

    class Meta:
        model = Performance
        fields = ['id', 'student', 'student_id', 'course_name', 'exam_marks', 'assignment_marks', 'attendance_percent', 'date_recorded']
