from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.models import AnonymousUser
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

    def get(self, request, **kwargs):
        if pk := kwargs.get('pk'):
            try:
                obj = Woman.objects.get(pk=pk)
                obj_sr = WomanSerializer(obj)
                return Response(
                                {'post': {'title': obj_sr.data.get('title'),
                                          'kind_name': obj_sr.data.get('kind_name')
                                          }
                                 }
                                )
            except:
                return Response({'error': 'Not exists'})
        obj = Woman.objects.all()
        return Response({'posts': WomanSerializer(obj, many=True).data})

    def post(self, request):
        serializer = WomanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'new_post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            return Response({'error': 'Method PUT is not allowed'})
        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})
        serializer = WomanSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'renewed post': serializer.data})

    def delete(self, request, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            return Response({'error': 'Method DELETE is not allowed'})
        try:
            deleting_obj = Woman.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})
        deleting_obj_sr = WomanSerializer(deleting_obj)
        deleting_obj.delete()
        return Response({'post deleted': {'title': deleting_obj_sr.data.get('title'),
                                          'kind_name': deleting_obj_sr.data.get('kind_name')
                                          }
                         }
                        )


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = LogIn()
        return context

