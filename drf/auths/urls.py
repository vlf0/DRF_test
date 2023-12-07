from django.urls import path
from . import api_views
from . import views


urlpatterns = [
    path('', views.IndexProfileView.as_view(), name='index'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('out/', views.CustomLogout.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('api/v1/womenlist/', api_views.WomanListAPIView.as_view()),
    path('api/v1/test/create/', api_views.WomanCreateAPIView.as_view()),
    path('api/v1/test/<int:pk>/', api_views.WomanDetailAPIView.as_view()),
]
