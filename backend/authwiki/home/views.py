from django.shortcuts import render, redirect

from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from multiprocessing import context

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .models import NewsletterSubscriber
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def homeview(request):
    return render(request, 'home/home.html')

def communityview(request):
    return render(request, 'home/communitypage.html')

def communityview_b(request):
    return render(request, 'home/communitypage2.html')

def communityview_c(request):
    return render(request, 'home/communitypage3.html')

def feedbackview(request):
    return render(request, 'home/feedback.html')

def errorview(request):
    return render(request, 'home/error.html')

def dashboardview(request):
    return render(request, 'home/dashboard.html')

@csrf_protect
def subscribe(request):
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        # Validate form data
        #if not email:
            #return HttpResponse('Please provide your email address.')

        # Save newsletter subscriber
        subscriber = NewsletterSubscriber.objects.create(sub_email=sub_email)
        #subscriber = NewsletterSubscriber(sub_email=sub_email,)
        #subscriber.save()
        return render(request, 'home/subscribed.html')

        #return HttpResponse('Thank you for subscribing to our newsletter!')
