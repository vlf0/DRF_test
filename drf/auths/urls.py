from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexProfileView.as_view(), name='index'),
    path('out/', views.CustomLogout.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('api/v1/womenlist/', views.WomanListAPIView.as_view()),
    path('api/v1/test/', views.WomanAPIView.as_view()),

]
