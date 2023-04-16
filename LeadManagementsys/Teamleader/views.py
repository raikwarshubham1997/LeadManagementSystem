from django.shortcuts import render, redirect
from django.http import HttpResponse
from StaffManager.models import Employee_Register
from Admin.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import mysql.connector
from django import forms
from operator import itemgetter
from .models import Worker_Register
from django.core.paginator import Paginator





def Employee(request):
    return render(request,"emp/dashboard.html")


# def login_emp(req):
#     con = mysql.connector.connect(host="localhost", user="root", password="", database="lead_systems")
#     cursor = con.cursor()
#     con2 = mysql.connector.connect(host="localhost", user="root", password="", database="lead_systems")
#     cursor2 = con2.cursor()
    

#     sqlcommand = "select username from leadadmin_employee_register"
#     sqlcommand2 = "select password from leadadmin_employee_register"
#     cursor.execute(sqlcommand)
#     cursor2.execute(sqlcommand2)

#     e =[]
#     p= []
#     for i in cursor:
#         e.append(i)
#     for j in cursor2:
#         p.append(j)

#     res = list(map(itemgetter(0), e))
#     res2 = list(map(itemgetter(0), p))
#     print(res)
#     print(res2)
#     if req.method == "POST":
#         username = req.POST['username']
#         password = req.POST['password']
#         i = 1
#         k=len(res)
#         while i < k:
#             if res[i]==username and res2[i]==password:
#                 print(username)
#                 return redirect('/employees/index/')
                # return render(req, 'emp/dashboard.html', {'username':username})
#                 break
#             i+=1
#         else:
#             messages.info(req, "Check username or password")
#             return redirect('/employees/emplogin/')
#     return render(req, 'emp/login.html')

class FormLogin(forms.Form):
    username = forms.CharField(label=("Username"), required=True)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput, required=True)

def login_emp(request):
    username = None
    form_login = FormLogin()
    if request.method == 'GET':
        if 'action' in request.GET:
            action =  request.GET.get('action')
            if action =='logout':
                if request.session.has_key('username'):
                    request.session.flush()
                return redirect('/teamleader/emplogin/')
            
        if 'username' in request.session:
            username = request.session['username']
            print(request.session.get_expiry_age())    # session lifetime in seconds (from now)
            print(request.session.get_expiry_date())   # datetime.datetime object which represent the moment in time at which
            
    elif request.method == 'POST':
        form_login = FormLogin(request.POST)
        print(form_login)
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            if username.strip() == username and password.strip() == password:
                request.session['username'] = username
                return render(request, 'emp/dashboard.html', {'demo_title': 'Session in Django', 'username':username})
                
            else:
                username = None
    
    return render(request, 'emp/login.html',{'form':form_login})
    


       
def logout_call(request):
	logout(request)
	return redirect('/logout/')



# Login SYSTEM for Worker 

def Worker_register(request):
    user = Employee_Register.objects.filter(id=4)
    print(user)
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pwd']
        create_by = request.POST['create']
        

        emp = Worker_Register(username=username,email=email,password=password,create_by_id=create_by)
        emp.save()
        messages.success(request, f"{username} Employee Register Successful")
        return redirect('/teamleader/register_user/')
    else:
        return render(request, 'emp/signup.html', {'user':user})
    
    
    
    
def get_all_lead(request):
    # user = Employee_Register.objects.filter(username=)
    # print("yes")
    # cobjs = LeadCreate.objects.all().order_by("id").reverse()
    # ServiceData = LeadCreate.objects.get()
    # paginator = Paginator(ServiceData, 6)
    # page_number = request.GET.get('page')
    # all_lead = paginator.get_page(page_number)
    # totalpage = all_lead.paginator.num_pages
    # # for i in all_lead:
    # #     print(i)
    # data = {
    #     'all_lead':all_lead,
    #     'lastpage':totalpage,
    #     'totalPagelist':[n+1 for n in range(totalpage)]
    # }
    return render(request, "emp/list_of_leads.html")