from django.db import models
from django.contrib.auth.models import User



class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)