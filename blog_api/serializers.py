from rest_framework import serializers
from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created",
            "category",
            "status",
            "slug",
        )
        model = Post




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
        )
        model = Category
