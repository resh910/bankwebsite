from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from . models import Form



# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('usr')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
              if User.objects.filter(username=username).exists():
                   messages.info(request,"username Taken")
                   return redirect('register')

              else:
                   user = User.objects.create_user(username=username,password=password)
                   user.save()
                   return redirect('login')
        else:
             messages.info(request,"password not matching")
             return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def form(request):
    if request.method == 'POST':
           first_name = request.POST.get('first_name')
           dateofbirth= request.POST.get('dateofbirth')
           age = request.POST.get('age')
           gender = request.POST.get('gender')
           email=request.POST.get('email')
           phonenumber = request.POST.get('phonenumber')
           address=request.POST.get('address')
           district=request.POST.get('district')
           branch=request.POST.get('branch')
           accounttype=request.POST.get('accounttype')
           materials=request.POST.get('materials')

           form=Form.objects.create(first_name = first_name,dateofbirth=dateofbirth,age=age,gender=gender,email=email,phonenumber=phonenumber,address=address,district=district,branch=branch,accounttype=accounttype,materials=materials)
           form.save()
           return redirect('msg')

    return render(request,"form.html")
def usr(request):
    return render(request,"user.html")

def msg(request):
    return render(request,"msg.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
