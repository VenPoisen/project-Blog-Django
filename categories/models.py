from django.db import models


class Category(models.Model):
    name_cat = models.CharField(max_length=50, verbose_name='Name')

    def __str__(self):
        return self.name_cat
