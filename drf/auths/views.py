from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .forms import UserLogInForm, CategoryCreatingForm, UserRegistrationForm
from .models import Category

CustomUser = get_user_model()


class UserRegistration(View):

    def get(self, request):
        return render(request, 'registration.html', {'reg_form': UserRegistrationForm()})

    def post(self, request):
        reg_data = UserRegistrationForm(request.POST)
        if reg_data.is_valid():
            username = reg_data.cleaned_data.get('name')

            if CustomUser.objects.filter(username=username):
                messages.info(request, 'This nickname already exists.')
                return redirect('registration')
            password = reg_data.cleaned_data.get('password')
            first_name = reg_data.cleaned_data.get('first_name')
            last_name = reg_data.cleaned_data.get('last_name')
            CustomUser.objects.create_user(username=username,
                                           password=password,
                                           first_name=first_name,
                                           last_name=last_name,
                                           is_active=True)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, 'Your account created success, Welcome!', extra_tags='acc_created')
            return redirect('profile')
        messages.info(request, 'Invalid data.')
        return redirect('registration')


class IndexProfileView(View):

    def get(self, request):
        return render(request, 'index.html', {'login_form': UserLogInForm()})

    def post(self, request):
        user = authenticate(username=request.POST.get('name'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('profile')
        messages.error(request, 'incorrect log/pass.')
        return render(request, 'index.html', {'login_form': UserLogInForm()})


class UserProfileView(View):

    def get(self, request):
        if not request.user.is_anonymous:
            return render(request, 'profile.html', {'new_category': CategoryCreatingForm})
        messages.info(request, 'Access not allowed. Please do authorizing.')
        return render(request, 'access.html')

    def post(self, request):
        if CategoryCreatingForm(request.POST).is_valid():
            new_category = Category(name=request.POST.get('name'))
            new_category.save()
            messages.info(request, f'New category {new_category.name} was added success', extra_tags='added')
            return render(request, 'profile.html', {'new_category': CategoryCreatingForm})


class CustomLogout(LogoutView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You are logged out.')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = UserLogInForm()
        return context

