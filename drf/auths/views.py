from django.contrib.auth import authenticate, get_user_model, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from .forms import LogIn, CategoryCreatingForm
from .models import Woman, Category
from rest_framework import generics


CustomUser = get_user_model()


def index(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('name'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('profile')
        messages.error(request, 'incorrect log/pass.')
    return render(request, 'index.html', {'login_form': LogIn()})


def profile(request):
    if request.method == 'POST':
        if CategoryCreatingForm(request.POST).is_valid():
            new_category = Category(name=request.POST.get('name'))
            new_category.save()
            messages.info(request, f'New category {new_category.name} was added success', extra_tags='added')
    return render(request, 'profile.html', {'new_category': CategoryCreatingForm})


class CustomLogout(LogoutView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = LogIn()
        return context

