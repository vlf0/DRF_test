from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializers import HospDataSerializer
from .psycopg2_module import BaseConnectionDB
from .additional_funcs import dataset_to_dict
from psycopg2.errors import SyntaxError


class HospDataBaseAPIView(APIView):
    """
    Base class for extension.

    Contains custom GET method only that getting data from DB.
    All you need - define that three attributes when you will extend this base class.

    Attributes:
    - raw_dataset: Received data from another database in the form of a list of tuples.
    - serializer_class: Concrete serializer for raw_dataset.
    - mapping_func: The first argument for map() function appropriate chosen serializer.
    When create a new class you need define this attribute as a argument of staticmethod, 
    like this: <transformation_func = staticmethod(mapping_func)>.
    """

    raw_dataset = None
    serializer_class = None

    def error_handler(self):
        if type(BaseConnectionDB()._get_columns_list()) is str:
            return {'Error': 'Dataset is not passed.'}
        elif not self.raw_dataset:
            return {'Error': 'Dataset is not passed.'}
        elif type(self.raw_dataset) is SyntaxError:
            return {'Error', str(self.raw_dataset)}
        elif not self.serializer_class:
            return {'Error': 'Serializer is not defined.'}

    def get(self, request):
        if self.error_handler():
            return Response(self.error_handler())
        columns_list = BaseConnectionDB()._get_columns_list()
        # In lambda func call  dataset_to_dict() with additional arg - column list
        # for zipping with dataset rows
        serializer = self.serializer_class(map(lambda item: dataset_to_dict(columns_list, item),
                                               self.raw_dataset), many=True)
        return Response({'data': serializer.data})
    

class ResearchListAPIView(HospDataBaseAPIView):
    permission_classes = [permissions.AllowAny]
    raw_dataset = BaseConnectionDB().execute_query('SELECT * FROM mm.dbkis;')
    serializer_class = HospDataSerializer


