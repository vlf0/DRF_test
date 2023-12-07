from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Woman
from .serializers import WomanSerializer, DeletedPostSerializer

CustomUser = get_user_model()


class WomanAPIView(APIView):

    def get(self, request, **kwargs):
        if pk := kwargs.get('pk'):
            try:
                obj = Woman.objects.get(pk=pk)
                obj_sr = WomanSerializer(obj)
                return Response(
                                {'post': {'title': obj_sr.data.get('title'),
                                          'kind_name': obj_sr.data.get('kind_name')
                                          }
                                 }
                                )
            except:
                return Response({'error': 'Not exists'})
        obj = Woman.objects.all()
        return Response({'posts': WomanSerializer(obj, many=True).data})

    def post(self, request):
        serializer = WomanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'new_post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            return Response({'error': 'Method PUT is not allowed'})
        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})
        serializer = WomanSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'renewed post': serializer.data})

    def delete(self, request, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            return Response({'error': 'Method DELETE is not allowed'})
        try:
            deleting_obj = Woman.objects.get(pk=pk)
        except:
            return Response({'error': 'Not exists'})
        deleting_obj_sr = WomanSerializer(deleting_obj)
        #  Writes row about deleting object in db
        deleted_post = DeletedPostSerializer(data={'row_id': deleting_obj.id, 'title': deleting_obj.title})
        deleted_post.is_valid(raise_exception=True)
        deleted_post.save()

        deleting_obj.delete()
        return Response({'post deleted': {'title': deleting_obj_sr.data.get('title'),
                                          'kind_name': deleting_obj_sr.data.get('kind_name')
                                          }
                         }
                        )


class WomanListAPIView(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer

