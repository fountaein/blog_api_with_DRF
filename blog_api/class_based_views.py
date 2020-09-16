from.models import Post, Category
from.serializers import PostSerializer , CategorySerializer
from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class PostLists(APIView):
    
    """
    List all posts, or create a new post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        posts= Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

   
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDetails(APIView):
    """
    Retrieve, update or delete a post instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        post = self.get_object(slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        post = self.get_object(slug)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        post = self.get_object(slug)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)