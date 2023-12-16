from rest_framework import serializers

INTEGER_FIELDS = ['id',
                  'ib_num']

CHAR_FIELDS = ['name',
               'doc_fio',
               'ib_num',
               'pat_fio',
               'research',
               'r_type',
               'dept',
               'status']

DATE_TIME_FIELDS = ['create_dt',
                    'dates2']


class HospDataSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    create_dt = serializers.DateTimeField(read_only=True)
    dates2 = serializers.DateTimeField(read_only=True)

    doc_fio = serializers.CharField(read_only=True)
    ib_num = serializers.IntegerField(read_only=True)
    pat_fio = serializers.CharField(read_only=True)
    research = serializers.CharField(read_only=True)
    r_type = serializers.CharField(read_only=True)
    dept = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    plan_dt = serializers.DateTimeField(read_only=True)




