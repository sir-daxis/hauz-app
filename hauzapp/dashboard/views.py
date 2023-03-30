from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm, LoginUserForm, UserPasswordResetForm


# Create your views here.

class LoginUser(auth_views.LoginView):
    model = User
    template_name = 'dashboard/pages/login_user.html'
    form_class = LoginUserForm
    success_url = '/'
    redirect_authenticated_user = True


class UserPasswordReset(auth_views.PasswordResetView):
    template_name = 'dashboard/pages/forgot_password.html'
    form_class = UserPasswordResetForm
    redirect_authenticated_user = True

@login_required
def base(request):
    return render(request, 'dashboard/includes/lorem.html')


def login_user(request):
    return render(request, 'dashboard/pages/login_user.html')


def forgot_password(request):
    return render(request, 'dashboard/pages/forgot_password.html')


def register_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard:home'))
    if request.method != 'POST':
        # Display blank registration form
        form = RegisterUserForm()
    else:
        form = RegisterUserForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # Log in new user
            login(request, new_user)
            return redirect('dashboard:home')

    # Display invalid or blank form
    return render(request, 'dashboard/pages/register_user.html', {'form': form})
