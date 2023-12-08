from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Woman, Category
from .serializers import WomanSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .permissions import *
CustomUser = get_user_model()


# class WomanViewSet(viewsets.ModelViewSet):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
#
#     # Set up custom permissions
#     def get_permissions(self):
#         if self.action == 'create':
#             permission_classes = [permissions.IsAuthenticated]
#         elif self.action in ['update', 'partial_update', 'destroy']:
#             permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
#         else:
#             permission_classes = [permissions.AllowAny]
#         return [permission() for permission in permission_classes]
#
#     def get_queryset(self):
#         if pk := self.kwargs.get('pk'):
#             return Woman.objects.filter(pk=pk)
#         return Woman.objects.all()
#
#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})


class WomanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomanUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class WomanDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    permission_classes = (IsAdminOrReadOnly,)
