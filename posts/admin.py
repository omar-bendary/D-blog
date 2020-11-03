from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ("title", "author", "created_on", "updated_on",)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
