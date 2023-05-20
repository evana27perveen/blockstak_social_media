from django.urls import path
from .views import (
    ProfileViewSet,
    ConnectionViewSet, PostListView, PostCreateView, PostDetailView, CommentListView, CommentCreateView, LikeListView,
    LikeCreateView, ShareListView, ShareCreateView, PostSearchView,
)

app_name = 'App_main'

urlpatterns = [
    path('profiles/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile-list'),
    path('profiles/my-operations/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='profile-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('likes/', LikeListView.as_view(), name='like-list'),
    path('likes/create/', LikeCreateView.as_view(), name='like-create'),
    path('shares/', ShareListView.as_view(), name='share-list'),
    path('shares/create/', ShareCreateView.as_view(), name='share-create'),
    path('posts/search/', PostSearchView.as_view(), name='post-search'),
    path('connections/', ConnectionViewSet.as_view({'get': 'list', 'post': 'create'}), name='connection-list'),
    path('connections/<int:pk>/', ConnectionViewSet.as_view({'get': 'retrieve'}), name='connection-detail'),
]

