from rest_framework import serializers
from .models import Woman


class WomanSerializer(serializers.ModelSerializer):
    kind_name = serializers.CharField(source='kind.name', read_only=True)

    class Meta:
        model = Woman
        fields = '__all__'

