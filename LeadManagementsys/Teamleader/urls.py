from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Employee),
    path('emplogin/', views.login_emp),
    path('register_user/<int:id>/', views.Worker_register),
    path('get_all_lead/', views.get_all_lead),

]