from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializers import HospDataSerializer
from .psycopg2_module import BaseConnectionDB
from .additional_funcs import dataset_to_dict
from .sql_queries import BaseSQLQueries, FilterSQLQueries
from psycopg2.errors import SyntaxError, UndefinedTable


class HospDataBaseAPIView(APIView):
    """
    Base class for extension.

    Contains custom GET method only that getting data from DB.
    All you need - define that three attributes when you will extend this base class.

    Attributes:
    - raw_dataset: Received data from another database in the form of a list of tuples.
    - serializer_class: Concrete serializer for raw_dataset.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = None

    def error_handler(self, **kwargs):
        if type(BaseConnectionDB()._get_columns_list(kwargs.get('tab'))) is str or None:
            return {'Error': 'Dataset is not passed.'}
        elif not kwargs:
            return {'Error': 'Method get is not allowed.'}
        elif not self.raw_dataset:
            return {'Error': 'Dataset is not passed.'}
        elif type(self.raw_dataset) in [SyntaxError, UndefinedTable]:
            return {'Error', str(self.raw_dataset)}
        elif not self.serializer_class:
            return {'Error': 'Serializer is not defined.'}

    def get(self, request, *args, **kwargs):
        self.raw_dataset = BaseConnectionDB().execute_query(kwargs.get('tab'))
        if self.error_handler(**kwargs):
            return Response(self.error_handler())

        columns_list = BaseConnectionDB()._get_columns_list(kwargs.get('tab'))
        # In lambda func call  dataset_to_dict() with additional arg - column list
        # for zipping with dataset rows

        serializer = self.serializer_class(map(lambda item: dataset_to_dict(columns_list, item),
                                               self.raw_dataset), many=True)
        return Response({'data': serializer.data})
    

class BaseListAPIView(HospDataBaseAPIView, BaseConnectionDB):
    permission_classes = [permissions.AllowAny]
    serializer_class = HospDataSerializer



