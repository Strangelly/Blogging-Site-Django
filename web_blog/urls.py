from django.urls import path
from .views import HomeView, ArticleView, AddPost, UpdatePost, DeletePost, AddCategory, CategoryView, CatDetailView

urlpatterns = [
    path('', HomeView.as_view(), name= 'home' ),
    path('article/<int:pk>', ArticleView.as_view(), name='article_detail'),
    path('post/', AddPost.as_view(), name='addpost'),
    path('category/', CategoryView.as_view(), name= 'category'),
    path('addcategory/', AddCategory.as_view(), name='addcats'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='editpost'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('category/<str:cats>/', CatDetailView, name='cat_detail'),
]