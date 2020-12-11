from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("microorganism", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("microorganism",)}
