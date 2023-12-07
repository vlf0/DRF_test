from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from .models import Woman
from .serializers import WomanSerializer

CustomUser = get_user_model()


class WomanViewSet(viewsets.ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


# class WomanDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
#
#
# class WomanCreateAPIView(generics.CreateAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
#
#
# class WomanListAPIView(generics.ListCreateAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer

