from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from posts.models import PostModel
# Create your views here.
class Post(ListView):
    model=PostModel
    template_name='index.html'
    # context_object_name: 'posts'
class PostCreate(CreateView):
    model=PostModel
    template_name='new_post.html'
    fields="__all__"
    # exlude=('user',)
class PostDetail(DetailView):
    model=PostModel
    template_name='detail_post.html'

class PostEdit(UpdateView):
    model=PostModel
    template_name='edit_post.html'
    fields=('title','body',)
class PostDelete(DeleteView):
    model=PostModel
    template_name='delete_post.html'
    def get_success_url(self):
        return reverse_lazy('post')
