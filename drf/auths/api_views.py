from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Woman, Category
from .serializers import WomanSerializer

CustomUser = get_user_model()


class WomanViewSet(viewsets.ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer

    def get_queryset(self):
        if pk := self.kwargs.get('pk'):
            return Woman.objects.filter(pk=pk)
        return Woman.objects.all()

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})



