from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,View
from .models import Post, Category
from .forms import PostForm
from .forms import EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['created_at']

class CategoryView(ListView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    #fields = '__all__'

class AddCategory(CreateView):
    model = Category
    template_name = 'addcats.html'
    fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatepost.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')

def CatDetailView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'cat_details.html', {'cats': cats.title(), 'category_post': category_post})