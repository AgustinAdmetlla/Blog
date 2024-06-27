from rest_framework import serializers
from .models import Post

class PostSerializer(serializer.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title', 
            'thumbnail',
            'excerpt',
            'content',
            'published',
            'author',
            'status',
            'slug',
        )












