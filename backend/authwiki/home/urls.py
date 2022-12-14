from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.homeview, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('community/', views.communityview, name='community'),
    path('community2/', views.communityview_b, name='community2'),
    path('community3/', views.communityview_c, name='community3'),
    path('feedback/', views.feedbackview, name='feedback'),
    path('error/', views.errorview, name='error'),
    path('dashboard/', views.dashboardview, name='dashboard'),
    ]
