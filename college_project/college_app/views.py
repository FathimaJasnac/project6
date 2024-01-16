from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import StudentApplicationForm
from .models import StudentApplication


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


# Create your views here.
def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpswd = request.POST['confirm password']
        if password == cpswd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('college_app:reg')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('college_app:login')

        else:
            messages.info(request, "password not matching")
            return redirect('college_app:reg')
        return redirect('/')
    return render(request, "register.html")


def student_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        mail_id = request.POST.get('mail_id')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials_provide = request.POST.get('materials_provide')
        form = StudentApplication(name=name, dob=dob, age=age, gender=gender, phone_number=phone_number,
                                  mail_id=mail_id, address=address, department=department,
                                  course=course, purpose=purpose, materials_provide=materials_provide)
        form.save()
        messages.success(request, 'Student added successfully!')

    else:
        form = StudentApplicationForm()
    return render(request, 'student_form.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('college_app:index')

def login(request):
    if request.method== 'POST':
        uname=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=uname,password=pswd)

        if user is not None:
            auth.login(request,user)
            return redirect('college_app:about')
        else:
            messages.info(request,"invalid registration")
            return redirect('college_app:login')
    return render(request,"login.html")
