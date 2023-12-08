from rest_framework import routers
from django.urls import path, include
from . import api_views
from . import views

w_router = routers.SimpleRouter()
w_router.register(r'test', api_views.WomanViewSet)

urlpatterns = [
    # URLs for simple django views (not API)
    path('', views.IndexProfileView.as_view(), name='index'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('out/', views.CustomLogout.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),

    # Using DRF routers
    path('api/v1/', include(w_router.urls)),
]
