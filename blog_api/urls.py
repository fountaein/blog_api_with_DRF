from django.urls import path

from.views import CategoryDetail, CategoryListView, PostListView, PostDetail

urlpatterns=[path('category/<int:pk>/', CategoryDetail.as_view()),
               path('category/', CategoryListView.as_view()),
               path('post/<str:slug>/<int:pk>', PostDetail.as_view(), name='post_detail'),
               path('post/', PostListView.as_view()),
               ]
