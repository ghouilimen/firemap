from django.contrib.auth import login
from django.urls import path,include
from .import views
from .views import home

urlpatterns=[
    path('', home , name='home'),
    path('register/',views.register , name='reg'),
    path('login/' , views.user_login, name='login')
]