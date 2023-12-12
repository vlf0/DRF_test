from rest_framework import serializers
from .models import Woman, DeletedPost, Category
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class WomanSerializer(serializers.ModelSerializer):
    kind_name = serializers.CharField(source='kind.name', read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Woman
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DeletedPostSerializer(serializers.Serializer):
    row_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    delete_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        deleted_post = DeletedPost.objects.create(**validated_data)
        return deleted_post


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


