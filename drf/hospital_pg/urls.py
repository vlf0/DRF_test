from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/hospdata/', views.HospDataAPIView.as_view(), name='get-data'),
]
