from django.core import serializers
from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'test',
            'created_date'
        )

    def create(self, validated_data):
        return Post.objects.create(validated_data)
