# Generated by Django 4.1.3 on 2022-12-01 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_alter_post_author_post_alter_post_category_post_and_more'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email_comment',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name_comment',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='publish_comment',
            field=models.BooleanField(default=False, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Username'),
        ),
    ]