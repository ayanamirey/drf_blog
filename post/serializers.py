from django.core import serializers
from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'id',
            'text',
            'created_date'
        )

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class PostTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
        )

    def create(self, validated_data):
        return Post.objects.create(validated_data)
