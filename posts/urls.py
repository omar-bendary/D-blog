from django.urls import path
from .views import BlogPostsView, BlogDetailView

urlpatterns = [
    path('', BlogPostsView.as_view(), name='post_list'),
    path('<uuid:pk>', BlogDetailView.as_view(), name='post_detail'),
]
