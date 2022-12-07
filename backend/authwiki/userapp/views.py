from django.shortcuts import render

# Create your views here.

def registerview(request):
    return render(request, 'userapp/register.html')

def loginview(request):
    return render(request, 'userapp/login.html')
