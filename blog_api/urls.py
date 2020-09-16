from django.urls import path

from.views import CategoryDetail, CategoryListView, PostListView, PostDetail
from blog_api import function_views
from blog_api.class_based_views import PostDetails, PostLists


urlpatterns=[path('category/<int:pk>/', CategoryDetail.as_view()),
               path('category/', CategoryListView.as_view()),
               path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
               path('post/', PostListView.as_view()),

               #FUNCTION BASED VIEWS
                path('posts/', function_views.post_lists),
                path('posts/<str:slug>/', function_views.post_details),

               #class based views
               path('blog_post/<str:slug>/', PostDetails.as_view(), name='post_detail'),
               path('blog_post/', PostLists.as_view()),
               ]

