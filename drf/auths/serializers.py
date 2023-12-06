from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Woman


# class WomanSerializer(serializers.ModelSerializer):
#     kind_name = serializers.CharField(source='kind.name', read_only=True)
#
#     class Meta:
#         model = Woman
#         fields = '__all__'


class WomenModel:

    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomanSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_alive = serializers.BooleanField(default=False)
    kind_id = serializers.IntegerField()
    #  Get the field from another model - Category
    kind_name = serializers.CharField(source='kind', read_only=True)

    def create(self, validated_data):
        return Woman.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_alive = validated_data.get('is_alive', instance.is_alive)
        instance.kind_id = validated_data.get('kind_id', instance.kind_id)
        instance.save()
        return instance


