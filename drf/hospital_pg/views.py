from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializers import HospDataSerializer
from .psycopg2_module import BaseConnectionDB
from .additional_funcs import dataset_to_dict


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

    def get(self, request):
        if not self.raw_dataset :
            return Response({'Error': 'Dataset is not passed.'})
        elif not self.serializer_class:
            return Response({'Error': 'Serializer is not defined.'})
        serializer = self.serializer_class(map(self.mapping_func, self.raw_dataset), many=True)
        return Response({'data': serializer.data})
    

class ResearchListAPIView(HospDataBaseAPIView):
    raw_dataset = BaseConnectionDB().execute_query('SELECT * FROM mm.dept;')
    serializer_class = HospDataSerializer
    transformation_func = staticmethod(dataset_to_dict)







