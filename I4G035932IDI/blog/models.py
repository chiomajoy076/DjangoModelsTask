from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

...
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(auto_now_add = True)
    
