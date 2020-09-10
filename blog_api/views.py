

from rest_framework import generics , permissions
from.models import Post, Category
from.serializers import PostSerializer , CategorySerializer
from .permissions import IsAuthorOrReadOnly

class PostListView(generics.ListCreateAPIView):
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    
    queryset=Post.objects.all()
    serializer_class= PostSerializer
  


class CategoryListView(generics.ListCreateAPIView):
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    
    queryset=Category.objects.all()
    serializer_class= CategorySerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class= PostSerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Category.objects.all()
    serializer_class= CategorySerializer