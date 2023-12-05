from rest_framework import serializers
from .models import Woman


class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman
        fields = '__all__'
