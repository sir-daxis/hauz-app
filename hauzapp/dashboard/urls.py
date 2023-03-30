from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.base, name='home'),
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('forgot-password/', views.UserPasswordReset.as_view(), name='forgot_password'),
    path('register/', views.register_user, name='register_user'),
]