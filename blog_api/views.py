

from rest_framework import generics 
from.models import Post, Category
from.serializers import PostSerializer , CategorySerializer

class PostListView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    paginate_by = 10


class CategoryListView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class= CategorySerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class= CategorySerializer