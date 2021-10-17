from django.shortcuts import render
from .forms import PostForm
from .models import post
from django.views.generic import ListView, CreateView

# Create your views here.


class PostListView(ListView):
    template_name = "gram/post_list.html"
    queryset = post.objects.all()
    context_object_name = "posts"

class PostCreateView(CreateView):
        template='gram/post_create.html'
        from_class = PostForm
        queryset = post.objects.all()
