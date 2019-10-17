from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,                           {'fields': ['title']}),
        (None,                           {'fields': ['image']}),
        (None,                           {'fields': ['private']}),
        (None,                           {'fields': ['user']}),
        ('Date Information',             {'fields': ['pub_date']})
    ]
    list_display = ('title', 'user', 'private', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Post, PostAdmin)