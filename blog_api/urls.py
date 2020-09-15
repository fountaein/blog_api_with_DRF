from django.urls import path

from.views import CategoryDetail, CategoryListView, PostListView, PostDetail
from blog_api import function_views
from blog_api.class_based_views import PostDetails, PostLists


urlpatterns=[path('category/<int:pk>/', CategoryDetail.as_view()),
               path('category/', CategoryListView.as_view()),
               path('post/<str:slug>/<int:pk>/', PostDetail.as_view(), name='post_detail'),
               path('post/', PostListView.as_view()),

               #FUNCTION BASED VIEWS
                path('posts/', function_views.post_lists),
                path('posts/<int:pk>/', function_views.post_detail),
                path('posts/<int:pk>/', function_views.update_delete_post),
                path('posts/', function_views.create_post),

               #class based views
               path('blog_post/<int:pk>/', PostDetails.as_view(), name='post_detail'),
               path('blog_post/', PostLists.as_view()),
               ]

