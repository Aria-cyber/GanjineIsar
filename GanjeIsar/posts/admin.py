from django.contrib import admin
from django.contrib.admin import StackedInline

from .models import Post,Comment


class CommentAdminInline(StackedInline):
    model = Comment
    fields = ['post','text']
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','text','avatar','created_time']
    list_filter = ['id']
    search_fields = ['id' , 'title']
    inlines = [CommentAdminInline]

admin.register(CommentAdminInline)
