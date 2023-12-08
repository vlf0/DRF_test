from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions, authentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import decorators
from rest_framework.response import Response
from .models import Woman, Category
from .serializers import WomanSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

CustomUser = get_user_model()


class WomanViewSet(viewsets.ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer

    # Set up custom permissions
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if pk := self.kwargs.get('pk'):
            return Woman.objects.filter(pk=pk)
        return Woman.objects.all()

    @decorators.action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})



