from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name="index.html"

class AddPost(CreateView):
    template_name="addpost.html"
    context_object_name="post"
    form_class=PostForm
    success_url=reverse_lazy('blogla')
    
    def form_valid(self,form):
        return super().form_valid(form)

class Posts(ListView):
    model=Post  
    template_name="list.html"
    context_object_name="post"
