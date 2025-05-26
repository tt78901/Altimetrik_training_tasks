from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, PerformanceForm
from .models import Student, Performance
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
import io
import base64
import matplotlib.pyplot as plt
import pandas as pd
from rest_framework import viewsets
from .serializers import StudentSerializer, PerformanceSerializer
def home(request):
   return render(request, 'home.html')
def is_staff_user(user):
   return user.is_staff
@user_passes_test(is_staff_user, login_url='/login/')
@login_required
def add_student(request):
   if request.method == 'POST':
       form = StudentForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
   else:
       form = StudentForm()
   return render(request, 'add_student.html', {'form': form})
@user_passes_test(is_staff_user, login_url='/login/')
@login_required
def add_performance(request):
   if request.method == 'POST':
       form = PerformanceForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
   else:
       form = PerformanceForm()
   return render(request, 'add_performance.html', {'form': form})
@login_required
def view_performance(request):
   performances = Performance.objects.all()
   return render(request, 'view_performance.html', {'performances': performances})
@login_required
def performance_charts(request):
   performances = Performance.objects.all().values(
       'student__name', 'course_name', 'exam_marks', 'assignment_marks', 'attendance_percent'
   )
   df = pd.DataFrame(performances)
   if df.empty:
       return HttpResponse("<h3>No data available to visualize yet.</h3>")
   avg_df = df.groupby('course_name')[['exam_marks', 'assignment_marks']].mean().reset_index()
   fig1, ax1 = plt.subplots()
   avg_df.plot(kind='bar', x='course_name', ax=ax1)
   ax1.set_title("📘 Average Marks per Course")
   ax1.set_ylabel("Marks")
   ax1.set_xlabel("Course")
   buf1 = io.BytesIO()
   plt.tight_layout()
   fig1.savefig(buf1, format='png')
   chart1 = base64.b64encode(buf1.getvalue()).decode('utf-8')
   buf1.close()
   plt.close(fig1)
   att_df = df.groupby('student__name')['attendance_percent'].mean().reset_index()
   fig2, ax2 = plt.subplots()
   att_df.plot(kind='line', x='student__name', y='attendance_percent', marker='o', ax=ax2)
   ax2.set_title("📈 Average Attendance by Student")
   ax2.set_ylabel("Attendance %")
   ax2.set_xlabel("Student")
   buf2 = io.BytesIO()
   plt.tight_layout()
   fig2.savefig(buf2, format='png')
   chart2 = base64.b64encode(buf2.getvalue()).decode('utf-8')
   buf2.close()
   plt.close(fig2)
   return render(request, 'performance_charts.html', {
       'chart1': chart1,
       'chart2': chart2,
   })
class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
class PerformanceViewSet(viewsets.ModelViewSet):
   queryset = Performance.objects.all()
   serializer_class = PerformanceSerializer

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_student(request, pk):
   student = get_object_or_404(Student, pk=pk)
   student.delete()
   return redirect('view_performance')

@login_required
@user_passes_test(lambda u: u.is_staff)
def update_student(request, pk):
   student = get_object_or_404(Student, pk=pk)
   if request.method == 'POST':
       form = StudentForm(request.POST, instance=student)
       if form.is_valid():
           form.save()
           return redirect('view_performance')
   else:
       form = StudentForm(instance=student)
   return render(request, 'update_student.html', {'form': form})