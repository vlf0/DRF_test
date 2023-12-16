from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/hospdata/', views.BaseListAPIView.as_view(), name='get-data'),
    path('api/v1/hospdata/<str:tab>/', views.BaseListAPIView.as_view(), name='get-data'),

]
