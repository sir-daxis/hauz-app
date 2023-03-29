from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('meetings:home'))
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # Log in new user
            login(request, new_user)
            return redirect('meetings:home')

    # Display invalid or blank form
    return render(request, 'registration/register.html', {'form': form})


# Create your views here.
