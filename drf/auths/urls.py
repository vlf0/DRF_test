from rest_framework import routers
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

w_router = routers.SimpleRouter()
# All automatic created urls from ViewSet
w_router.register(r'test', views.WomanViewSet)

urlpatterns = [
    # # rest auth
    # path('api/v1/user/', include('rest_framework.urls')),

    # REST Token auth
    path('api/v1/token/', obtain_auth_token, name='get-token'),

    # Using DRF routers
    path('api/v1/', include(w_router.urls)),
]
