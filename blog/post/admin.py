from django.contrib import admin
from .models import Topic, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic_name', 'created_date', 'published_date', 'slug']
    list_display_links = ['title']
    list_filter = ['published_date']
    search_fields = ['title', 'text']
    list_editable = ['topic_name']

    class Meta:
        model = Post


admin.site.register(Topic)
admin.site.register(Post, PostAdmin)
