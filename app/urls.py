from django.contrib import admin
from django.urls import path, include
from . views import*

urlpatterns = [
    path('', homepage, name='home'),
    path('test', TestView.as_view(), name='test'),
    # path('overview', overview, name='overview'),

    # api 
    path('user_register', UserRegisterView.as_view(), name='user_register'),
]
