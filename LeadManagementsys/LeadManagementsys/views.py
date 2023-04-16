from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail



def SignUp(request):
    if request.method == 'POST':
        name = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pwd']
        date = datetime.now()
        
        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already taken')
            return redirect('/')
        else:
            uobj = User(first_name=name, last_name=lname, email=email, username=username, password=make_password(password), is_staff=True, date_joined=date)
            uobj.save()
            data= uobj.first_name
            messages.success(request, f"{data} Your Account Has Been Created!")
            send_mail(
                    'Response Mail',
                    f'Hi {name} \nWeclcome to Our Lead Management System Your User Account Has been Created successfully.\nUsername: {username}\nPassword: {password}',
                    'techpanda.sr@gmail.com',
                    [email],
                    fail_silently=False,
                )
            return redirect('/')
    else:
        return render(request, 'signup.html')


def login_sys(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        print(uname)
        user = authenticate(username=uname, password=pwd)
        # print(user.date_joined)

        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('/superadmin/')
            elif user.is_staff:                                 # Admin
                return redirect('/admins/')
            elif user.is_manager:
                return redirect('/leadadmin/')
            
        else:
            return redirect('/')
    
    return render(request, "login.html")
	

def logout_call(request):
	logout(request)
	return redirect('/login/')


    # if request.method =='POST':
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     uobjs = authenticate(username=username, password=password)
        
    #     if uobjs:
    #         login(request, uobjs)
    #         if uobjs.is_superuser:
    #             return redirect('/superadmin/')
    #         elif uobjs.is_staff:
    #             return redirect('/employees/')
    #     else:
    #         return redirect('/')
    # else:
    #     return render(request, "login.html")