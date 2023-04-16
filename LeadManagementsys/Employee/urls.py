from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('get_all_lead/', views.get_all_lead),
#     path('show_leadinfo/<int:id>/', views.ShowLeadInfo, name='show_leadinfo'),
#     path('edit_leadinfo/<int:id>/', views.EditLeadInfo, name='edit_leadinfo'),
#     path('delete_leadinfo/<int:id>/', views.DeleteLeadInfo, name='delete_leadinfo'),
]