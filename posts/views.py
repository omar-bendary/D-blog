from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import CommentForm

# Create your views here.


class BlogPostsView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'body', 'image',)
    template_name = 'posts/post_edit.html'

    # login required
    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')

    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'body', 'image',)
    template_name = 'posts/post_new.html'

    login_url = 'account_login'

    # author prefilled

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(CreateView):
    model = Comment

    fields = ('body',)
    template_name = 'posts/comment_new.html'

    # post prefilled
    def form_vaild(self, form):
        form.instace.post_id = self.kwargs['pk']
        return super().form_valid(form)

    # author prefilled

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
