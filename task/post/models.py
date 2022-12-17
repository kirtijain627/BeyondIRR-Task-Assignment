# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=20, choices=(('draft','Draft'), ('published', 'Published'), ('archived', 'Archived')))
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Notification(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)