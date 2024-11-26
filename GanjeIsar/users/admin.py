from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import  MyUser
@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','phone_number','date_joined']
    list_filter = ['id']
    search_fields = ['id' , 'phone_number']
# @admin.register(MyUser)
# class MyUserAdmin(UserAdmin):
#     # fieldsets = (
#     #     ('phone number' , {'fields':'phone_number'}),
#     #     ('nick name' , {'fields' :'username'}),
#     #     ('others' , {'fields': ('is_staff','date_joined')})
#     #
#     #
#     # )
#     # add_fieldsets = (
#     #     (None , {
#     #
#     #         'classes':('wide'),
#     #         'fields':('uaername' , 'phone_number' )
#     #
#     #     })
#     # )
#     list_display = ['username','phone_number','is_staff','date_joined']
#     list_filter = ['id']
#     search_fields = ['id', 'phone_number']