from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('', include('django.contrib.auth.urls')),  # Include default auth urls.
    path('register/', views.register, name='register'),
]