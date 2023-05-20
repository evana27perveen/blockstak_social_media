from django.urls import path

app_name = 'App_main'

urlpatterns = [
  path('profiles/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile-list'),
  path('profiles/my-operations/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='profile-detail'),
]
