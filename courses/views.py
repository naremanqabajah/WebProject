from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Student, Course, CourseSchedule, StudentReg
from django.contrib import messages
from django.db import IntegrityError

def home(request):
    if 'student_id' not in request.session:
        return redirect('login')
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            student = Student.objects.get(email=email, password=password)
            request.session['student_id'] = student.id
            return redirect('home')
        except Student.DoesNotExist:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if Student.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('register')

        student = Student(name=request.POST['name'], email=email, password=password)
        student.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'register.html')

def courses(request):
    if 'student_id' not in request.session:
        return redirect('login')
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def add_course(request):
    if 'student_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        description = request.POST.get('description')
        prerequisites = request.POST.get('prerequisites')
        instructor = request.POST.get('instructor')
        capacity = request.POST.get('capacity')
        schedule = request.POST.get('schedule')

        try:
            course = Course.objects.create(
                code=code,
                name=name,
                description=description,
                prerequisites=prerequisites,
                instructor=instructor,
                capacity=capacity
            )
            student = Student.objects.get(id=request.session['student_id'])
            StudentReg.objects.create(student=student, course=course)
            messages.success(request, 'Course added and registered successfully')
            return redirect('courses')
        except IntegrityError:
            messages.error(request, 'Course code must be unique.')

    return render(request, 'add_course.html')

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    messages.success(request, 'Course deleted successfully')
    return redirect('courses')

def search_course(request):
    if 'student_id' not in request.session:
        return redirect('login')
    # Implement search functionality here
    return render(request, 'search_course.html')


def search_course(request):
    query = request.GET.get('course_name', '')
    courses = Course.objects.filter(name__icontains=query) if query else None
    return render(request, 'search_course.html', {'courses': courses, 'query': query})