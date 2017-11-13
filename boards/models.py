from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

class Discussion_Board(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Discussion(models.Model):
    subject = models.CharField(max_length=255)
    started_by = models.ForeignKey(User, related_name='topics')
    board = models.ForeignKey(Discussion_Board, related_name='topics')
    last_updated = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length = 2000)
    topic = models.ForeignKey(Discussion, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
