from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializers import HospDataSerializer
from .psycopg2_module import BaseConnectionDB, ChangingQueriesDB
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
    cursor = BaseConnectionDB
    # query = BaseSQLQueries
    serializer_class = None
    raw_data = None

    def error_handler(self, **kwargs):
        # if type(self.raw_data) is str:
        #     return {'Error': 'Dataset is not passed.'}
        # if not kwargs:
        #     return {'Error': 'Method get is not allowed.'}
        if not self.cursor:
            return {'Error': 'Dataset is not passed.'}
        elif not self.serializer_class:
            return {'Error': 'Serializer is not defined.'}
        elif type(self.raw_data) in [SyntaxError, UndefinedTable, str]:
            return {'Error', str(self.raw_data)}

    def get(self, request, *args, **kwargs):
        self.raw_data = self.cursor().execute_query(kwargs.get('tab')) if kwargs \
            else 'Method get is not allowed.'
        if self.error_handler(**kwargs):
            return Response(self.error_handler())
        # self.raw_data = self.cursor().execute_query(kwargs.get('tab'))
        columns_list = self.cursor()._get_columns_list(kwargs.get('tab'))
        # In lambda func call  dataset_to_dict() with additional arg - column list
        # for zipping with dataset rows
        serializer = self.serializer_class(map(lambda item: dataset_to_dict(columns_list, item),
                                               self.raw_data), many=True)
        return Response({'data': len(serializer.data)})
    

class BaseListAPIView(HospDataBaseAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = HospDataSerializer
    # cursor = ChangingQueriesDB
    # query = FilterSQLQueries


