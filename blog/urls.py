from django.urls import path
from . import views 
from .views import (
    PostListView ,
    PostDetailView ,
    PostCreateView ,
    PostUpdateView ,
    PostDeleteView ,
    userPostListView
)





urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # to import view list You must << 'app_name'/'model_name'_list.html >>
    path('user/<str:username>', userPostListView.as_view(), name='user-posts'), # make url for users that making posts
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'), # Details Page
    path('post/new/', PostCreateView.as_view(), name='post-create'), # create Page
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Update Page
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete Page
    path('about/', views.about, name='blog-about'),
]

