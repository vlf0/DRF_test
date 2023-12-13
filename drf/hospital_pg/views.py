from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializers import HospDataSerializer
from .psycopg2_module import BaseConnectionDB
from .additional_funcs import dataset_to_dict


class HospDataAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    raw_dataset = BaseConnectionDB().execute_query('SELECT * FROM mm.dept;')

    def get(self, request):
        print(self.raw_dataset)
        serializer = HospDataSerializer(map(dataset_to_dict, self.raw_dataset), many=True)
        print(serializer.data)
        return Response({'data': serializer.data})






