from rest_framework import routers
from django.urls import path, include
from . import views

# w_router = routers.SimpleRouter()
# w_router.register(r'test', api_views.WomanViewSet)

urlpatterns = [

    # Using API views
    path('api/v1/test/', views.WomanListCreateAPIView.as_view()),
    path('api/v1/test/<int:pk>/', views.WomanUpdateAPIView.as_view()),
    path('api/v1/testdelete/<int:pk>/', views.WomanDeleteAPIView.as_view()),

    # Using DRF routers
    # path('api/v1/', include(w_router.urls)),
]
