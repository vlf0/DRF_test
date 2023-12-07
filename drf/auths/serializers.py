from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Woman, DeletedPost


# class WomanSerializer(serializers.ModelSerializer):
#     kind_name = serializers.CharField(source='kind.name', read_only=True)
#
#     class Meta:
#         model = Woman
#         fields = '__all__'


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


class DeletedPostSerializer(serializers.Serializer):
    row_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    delete_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        deleted_post = DeletedPost.objects.create(**validated_data)
        return deleted_post

