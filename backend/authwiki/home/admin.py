from django.contrib import admin
from . models import NewsletterSubscriber

#class SubscribedUsersAdmin(admin.ModelAdmin):
#    list_display = ('emails', 'created_date')
# Register your models here.
admin.site.register(NewsletterSubscriber)
