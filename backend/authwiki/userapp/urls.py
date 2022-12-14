from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from userapp.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from userapp.forms import LoginForm

from home.views import homeview
from .views import profile, RegisterView
from . import views
from django.urls import reverse_lazy

app_name = 'userapp'

urlpatterns = [

        path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='home/login.html',
                                           authentication_form=LoginForm), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='home/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    #re_path(r'^oauth/', include('social_django.urls', namespace='social')),

    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('emailverification/', views.emailverification, name='emailverification'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
