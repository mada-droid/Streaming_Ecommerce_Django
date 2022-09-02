from rest_framework import serializers

from blog.models import BlogPost


class BlogPostSerializer(serializers.Serializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content']