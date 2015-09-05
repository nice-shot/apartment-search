"""
Holds the poll module
"""
from django.db import models

class Post (models.Model):
    post_id = models.CharField(max_length=100, primary_key=True)
    message = models.TextField()
    user = models.CharField(max_length=300)
    likes = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    found_time = models.DateTimeField(auto_now_add=True)
    interesting = models.NullBooleanField()
