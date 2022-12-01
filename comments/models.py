from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.utils import timezone


class Comment(models.Model):
    name_comment = models.CharField(max_length=120, verbose_name='Name')
    email_comment = models.EmailField(verbose_name='Email')
    comment = models.TextField(verbose_name='Comment')
    post_comment = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Post')
    user_comment = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Username')
    date_comment = models.DateTimeField(
        default=timezone.now, verbose_name='Date')
    publish_comment = models.BooleanField(
        default=False, verbose_name='Publish')

    def __str__(self):
        return self.name_comment
