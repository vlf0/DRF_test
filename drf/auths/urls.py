from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('out/', views.CustomLogout.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

]
