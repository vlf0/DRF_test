from rest_framework import routers
from django.urls import path, include
from . import views

w_router = routers.SimpleRouter()
w_router.register(r'test', views.WomanViewSet)

urlpatterns = [
    # rest auth
    path('api/v1/user/', include('rest_framework.urls')),

    # Using DRF routers
    path('api/v1/', include(w_router.urls)),
]
