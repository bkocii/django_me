from django.shortcuts import render, redirect
from .forms import RegisterStudent
from .models import Students
from django.contrib import messages


def index(request):
    return render(request, 'boot/index.html')


def register(request):
    if request.method == 'POST':
        student = RegisterStudent(request.POST)
        if student.is_valid():
            student.save()
        return redirect(index)
    messages.success(request, '✔ You Have Registered Four Our Course.')
    return render(request, 'boot/register.html', {'form': RegisterStudent})
