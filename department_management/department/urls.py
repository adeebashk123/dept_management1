# department/urls.py

from django.urls import path
from . import views
from .views import login_view, logout_view,home


urlpatterns = [
    path('home', home, name='home'), 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_department/', views.add_department, name='add_department'),
    path('modify/<int:department_id>/', views.modify_department, name='modify_department'),
    path('delete/<int:department_id>/', views.delete_department, name='delete_department'),
]
