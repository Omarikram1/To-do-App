from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
  
     path('', views.landingpage, name='landingpage'),
     path('login/', views.loginpage, name='login'),
     path('signup', views.signuppage, name='signup'),
     path('home', views.homepage, name='home'),
     path('deletetask/<int:task_id>/', views.deletetask, name='deletetask'),
     path('addtask', views.addtask, name='addtask'),
     path('updatetask/<int:task_id>/', views.updatetask, name='updatetask'),
     path('taskcompleted/<int:task_id>/', views.taskcompleted, name='taskcompleted'),
]


