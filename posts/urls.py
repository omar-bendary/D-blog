from django.urls import path
from .views import BlogPostsView, BlogDetailView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('', BlogPostsView.as_view(), name='post_list'),
    path('<uuid:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('<uuid:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_new'),
]
