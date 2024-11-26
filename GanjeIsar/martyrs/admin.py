from django.contrib import admin

from .models import Martyr

@admin.register(Martyr)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','avatar']
    list_filter = ['id']
    search_fields = ['id' , 'title']
