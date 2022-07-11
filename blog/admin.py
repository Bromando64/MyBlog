from django.contrib import admin

from blog.models import Author, Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date", "author",)
    list_filter = ("author", "tags", "date",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post",)
# Register your models here.


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
