from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

cats = []

for item in choices:
    cats.append(item)

#cats = [ ('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment'), ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','comment', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices= cats, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'comment': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','comment','body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'comment': forms.Select(attrs={'class': 'form-control'}),
        }