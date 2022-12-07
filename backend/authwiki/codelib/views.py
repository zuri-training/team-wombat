from django.shortcuts import render

# Create your views here.

def resourceview(request):
    return render(request, 'codelib/resource.html')

