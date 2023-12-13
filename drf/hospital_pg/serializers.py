from rest_framework import serializers


class HospDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    date1 = serializers.DateTimeField(read_only=True)
    date2 = serializers.DateTimeField(read_only=True)

