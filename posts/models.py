from django.db import models
from django.contrib.auth.models import User

class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)