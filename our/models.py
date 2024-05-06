from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser






class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    nomi = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rasm = models.ImageField(upload_to='yangilik/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    bolim = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.nomi
    

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    rasm = models.ImageField(upload_to='yangilik/', null=True, blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bolim = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    izoh = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.izoh




# Create your models here.
