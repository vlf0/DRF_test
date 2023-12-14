from django.urls import path, include
from . import views


urlpatterns = [
    path('api/v1/hospdata/', views.ResearchListAPIView.as_view(), name='get-data'),
]
