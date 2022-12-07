from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_post', 'author_post', 'date_post',
                    'category_post', 'publish_post')
    list_editable = ('publish_post',)
    list_display_links = ('id', 'title_post',)


admin.site.register(Post, PostAdmin)
