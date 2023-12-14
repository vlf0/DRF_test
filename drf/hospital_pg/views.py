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
    mapping_func = None

    def error_handler(self):
        if not self.raw_dataset:
            return {'Error': 'Dataset is not passed.'}
        elif type(self.raw_dataset) is SyntaxError:
            return {'Error', str(self.raw_dataset)}
        elif not self.serializer_class:
            return {'Error': 'Serializer is not defined.'}
        elif not self.mapping_func:
            return {'Error': 'Mapping function is not defined.'}

    def get(self, request):
        if self.error_handler():
            return Response(self.error_handler())
        
#TODO: Need to create and implement custom serializer for PG data
#TODO: and mapping column list with dataset list in one the same dict.  

        # Works while explicitly defined  mapping_func attribute.
        serializer = self.serializer_class(map(self.mapping_func, self.raw_dataset), many=True)
        return Response({'data': serializer.data})
    

class ResearchListAPIView(HospDataBaseAPIView):
    raw_dataset = BaseConnectionDB().execute_query('SELECT * FROM mm.dept;')
    serializer_class = HospDataSerializer
    mapping_func = staticmethod(dataset_to_dict)







