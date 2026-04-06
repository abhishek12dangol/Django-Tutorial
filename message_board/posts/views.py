from django.shortcuts import render
from .models import Post, Test
from django.views.generic import ListView

# Create your views here.
#def post_list(request):
#    posts = Post.objects.all()
#    return render(request, "post_list.html", {"posts": posts})

class PostList(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"