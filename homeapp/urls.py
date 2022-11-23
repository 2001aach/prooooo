from django.urls import path

from homeapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('user',views.user,name='user'),
    path('worker',views.worker,name='worker'),
    path('userregister',views.userregister,name='userregister'),
    path('workerregister',views.workerregister,name='workerregister')
]