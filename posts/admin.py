from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on", "updated_on",)


admin.site.register(Post, PostAdmin)
