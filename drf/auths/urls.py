from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:status>/', views.index, name='index'),
    # path('bye/', views.LogoutView.as_view(), name='logout'),
    path('bye/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
]
