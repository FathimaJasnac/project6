from django.contrib import messages
from django.shortcuts import render, redirect
from clgapp.forms import StudentForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "order confirmed")
            return render(request,'student_form.html',{'form': form})
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
