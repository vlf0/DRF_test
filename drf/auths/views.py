from django.contrib.auth import authenticate, get_user_model, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.views import View
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import LogIn, CategoryCreatingForm
from .models import Woman, Category
from .serializers import WomanSerializer

CustomUser = get_user_model()


class WomanAPIView(APIView):

    def get(self, request):
        obj = Woman.objects.all().values()
        return Response({'posts': list(obj)})

    def post(self, request):
        new_obj = Woman.objects.create(
            title=request.data.get('title'),
            content=request.data.get('content'),
            is_alive=request.data.get('is_alive'),
            kind_id=request.data.get('kind_id')
        )
        return Response({'new_post': model_to_dict(new_obj)})


class WomanListAPIView(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer



class IndexProfileView(View):

    def get(self, request):
        return render(request, 'index.html', {'login_form': LogIn()})

    def post(self, request):
        user = authenticate(username=request.POST.get('name'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('profile')
        messages.error(request, 'incorrect log/pass.')
        return render(request, 'index.html', {'login_form': LogIn()})


class UserProfileView(View):

    def get(self, request):
        return render(request, 'profile.html', {'new_category': CategoryCreatingForm})

    def post(self, request):
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

