from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_date', 'writer')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'writer')
    list_per_page = 10
admin.site.register(Post, PostAdmin)