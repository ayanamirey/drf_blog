from django.http import JsonResponse, Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from post.models import Post
from post.serializers import PostSerializer, PostTitleSerializer


class PostList(APIView):
    def get(self, request, format=None):
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def post_title_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostTitleSerializer(posts, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def post_detail(request, pk):
#     if request.method == 'GET':
#         posts = Post.objects.get(pk=pk)
#         serializer = PostSerializer(posts)
#         return Response(serializer.data)
