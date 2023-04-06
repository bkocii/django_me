from django.shortcuts import render, redirect
from .forms import RegisterStudent
from .models import Students, Course
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
import os


def index(request):
    return render(request, 'boot/index.html')


def register(request):
    if request.method == 'POST':
        student = RegisterStudent(request.POST)
        if student.is_valid():
            student.save()
            messages.success(request, '✔ You Have Registered Four Our Course.')
        return redirect(index)
    return render(request, 'boot/register.html', {'form': RegisterStudent})


@staff_member_required
@login_required
def send_email(request):
    students = Students.objects.all()
    courses = Course.objects.all()
    context = {
        'students': students,
        'courses': courses
    }
    if request.method == 'POST':
        select = request.POST.get('select')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        active = request.POST.get('is_active')
        print(active)
        if active == 'active':
            if select == 'All groups':
                students_to_email = Students.objects.filter(is_active=True)
            else:
                students_to_email = Students.objects.filter(course_name__course_name=select, is_active=True)
        elif active == 'not_active':
            if select == 'All groups':
                students_to_email = Students.objects.filter(is_active=False)
            else:
                students_to_email = Students.objects.filter(course_name__course_name=select, is_active=False)
        else:
            if select == 'All groups':
                students_to_email = Students.objects.filter()
            else:
                students_to_email = Students.objects.filter(course_name__course_name=select)
        for i in range(len(students_to_email)):
            send_mail(
                subject,
                message,
                os.environ.get('GMAIL_USERNAME'),
                [students_to_email[i].email],
                fail_silently=False,
            )
        if len(students_to_email) == 0:
            messages.error(request, 'No students for the chosen selection!')
        else:
            messages.success(request, '✔ Email has been sent.')
        return render(request, 'boot/send_email.html', context)
    return render(request, 'boot/send_email.html', context)
