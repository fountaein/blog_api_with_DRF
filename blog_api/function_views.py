from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from.models import Post, Category
from.serializers import PostSerializer , CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_lists(request):

    """
    List all posts or create a new post.
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    
@api_view(['GET','PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_details(request, slug):
    """
    update or delete a single post.
    """
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)