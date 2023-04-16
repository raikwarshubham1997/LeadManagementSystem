from django.urls import path
from . import views

urlpatterns = [    
    path('', views.LeadAdmin),
    path('register_emp/', views.Emp_register),
    path('myLeads/', views.ManagerLeads),
    path('managelogin/', views.login_emp),
    path('export_lead/', views.Export_xlsx),
    path('showinfo/<int:id>/', views.ShowLeadInfo, name="show_leadinfo"),

    path('edit_leadinfo/<int:id>/', views.EditLeadInfo, name='edit_leadinfo'),
    
    path('delete_leadinfo/<int:id>/', views.DeleteLeadInfo, name='delete_leadinfo'),

]