from django.contrib.auth import authenticate, get_user_model, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView


from .forms import LogIn

CustomUser = get_user_model()


def index(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('name'), password=request.POST.get('password'))
        if user is not None:
            return redirect('profile')
        messages.error(request, 'incorrect log/pass.')
    return render(request, 'index.html', {'login_form': LogIn()})


def profile(request):
    return render(request, 'profile.html')


def log_out(request):
    logout(request)
    messages.success(request, 'You are logged out.')

    return redirect('index')
