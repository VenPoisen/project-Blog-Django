from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
import os


class Post(models.Model):
    title_post = models.CharField(max_length=255, verbose_name='Title')
    author_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Author')
    date_post = models.DateTimeField(default=timezone.now, verbose_name='Date')
    content_post = RichTextUploadingField(verbose_name='Content')
    summary_post = models.TextField(verbose_name='Summary')
    category_post = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Category')
    image_post = models.ImageField(
        upload_to=r'post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Image')
    publish_post = models.BooleanField(default=False, verbose_name='Publish')

    def __str__(self):
        return self.title_post

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.resize_image(self.image_post.name, 800)

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60,
        )
        new_img.close()
