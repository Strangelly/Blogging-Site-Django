from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    username = models.CharField(max_length=255)
    comment = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="post_comments")
    media = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="post_media")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255, default='coding')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        #return reverse('article_detail', args=(str(self.id)))
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')



# Comment model
class Comment(models.Model):
    content = models.TextField()
    author_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    media = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id} by {self.author_username}"
    
# Media model
class Media(models.Model):
    content = models.BinaryField()

    def __str__(self):
        return f"Media {self.id}"

