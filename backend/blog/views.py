from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        # posts = Post.objects.all()
        posts = Post.postobjects.all() 

        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)


class PostDetailView(APIView):

    def get(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)












