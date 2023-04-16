"""LeadManagementsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadmin/', include('SuperAdmin.urls')),
    path('admins/', include('Admin.urls')),
    path('staffmanag/', include('StaffManager.urls')),
    path('teamleader/', include('Teamleader.urls')),
    path('employees/', include('Employee.urls')),
    path('employee_register/', views.SignUp),
    path('', views.login_sys),
    path('logout/', views.logout_call, name='logout')

]
