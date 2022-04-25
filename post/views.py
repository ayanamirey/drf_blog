from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Post
from post.serializers import PostSerializer, PostTitleSerializer


@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_title_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostTitleSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, pk):
    if request.method == 'GET':
        posts = Post.objects.get(pk=pk)
        serializer = PostSerializer(posts)
        return Response(serializer.data)
