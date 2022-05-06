from django.contrib import admin
from blog.models import Post, Tag, PostTag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'user_id']
    list_filter = ['created_time', 'user_id']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class PostTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'tag_id']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PostTag, PostTagAdmin)
