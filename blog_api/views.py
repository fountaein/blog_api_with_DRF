

from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly

from.models import Post, Category
from.serializers import PostSerializer , CategorySerializer



@api_view()
def redirection_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def success_view(request):
    return Response("Email account is activated")

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
