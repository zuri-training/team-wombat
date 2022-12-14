from django.db import models
from django.utils import timezone

# Create your models here.
#class SubscribedUsers(models.Model):
#    emails = models.EmailField(unique=True, max_length=100)
#    created_date = models.DateTimeField('Date created', default=timezone.now)
#
#    def __str__(self):
#        return self.emails

class NewsletterSubscriber(models.Model):
    sub_email = models.EmailField(unique=True, max_length=100)
    active = models.BooleanField(default=True)
    subscription_date = models.DateTimeField(auto_now_add=True)
