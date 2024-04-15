from django.contrib import admin

from news.models import *

class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_time', 'rating')
    list_filter = ('author', 'created_time', 'rating')


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Post, PostsAdmin)
