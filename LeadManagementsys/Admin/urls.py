from django.urls import path
from . import views

urlpatterns = [

    path('manager/', views.SignUp),
    path('get_users/', views.Get_all_users),
    path('userdetails/<int:id>/', views.UserDetails, name="view_detail"),
    path('new_lead/', views.CreateLeads),
    path('get_all_lead/', views.get_all_lead),
    path('show_leadinfo/<int:id>/', views.ShowLeadInfo, name='show_leadinfo'),
    path('edit_leadinfo/<int:id>/', views.EditLeadInfo, name='edit_leadinfo'),
    path('delete_leadinfo/<int:id>/', views.DeleteLeadInfo, name='delete_leadinfo'),

    path('upload_file/', views.simple_upload),
    path('export_lead/', views.Export_xlsx),
    path('demofile/', views.Demo_xlsx),
    


    path('call_logs_create/<int:id>/',views.CallLogs, name='call_log'),
    path('edit_loginfo/<int:id>/', views.Edit_callLog, name='edit_log'),
    path('delete_loginfo/<int:id>/', views.Delete_log, name='delete_log'),


    path('notes_create/<int:id>/',views.Notes_CallLogs, name='notes'),
    path('notes_edit/<int:id>/',views.Edit_Note, name='edit_notes'),
    
    

    path('', views.Admin),
    
]