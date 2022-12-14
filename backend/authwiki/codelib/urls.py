from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'codelib'

urlpatterns = [
    path('resource/', views.resourceview, name='resource'),
    ]
