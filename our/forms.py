from django import forms
from django.contrib.auth.models import User
from .models import Book,Category,News,Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['nomi', 'rasm', 'bolim']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'rasm', 'bolim']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['izoh']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

