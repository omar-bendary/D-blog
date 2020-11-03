from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post
# Create your views here.


class HomePostsView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'post_list'
