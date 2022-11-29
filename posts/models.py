from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title_post = models.CharField(max_length=255, verbose_name='Title')
    author_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Author')
    date_post = models.DateTimeField(default=timezone.now, verbose_name='Date')
    content_post = models.TextField(verbose_name='Content')
    summary_post = models.TextField(verbose_name='Summary')
    category_post = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Category')
    image_post = models.ImageField(
        upload_to=r'post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Image')
    publish_post = models.BooleanField(default=False, verbose_name='Publish')

    def __str__(self):
        return self.title_post
