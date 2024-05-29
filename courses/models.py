from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    prerequisites = models.CharField(max_length=255, blank=True)
    instructor = models.CharField(max_length=255)
    capacity = models.IntegerField()
    schedule = models.CharField(max_length=255)  # تعديل الكلمة إلى max_length

class CourseSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    days = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=50)

class StudentReg(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
