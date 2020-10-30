from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, DetailView
# Create your views here.


class BlogPostsView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'


class BlogDetailView(DetailView):
    pass
