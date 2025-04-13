from django.contrib import admin

from posts.models import Author, Category, Post



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user']

admin.site.register(Author, AuthorAdmin)

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'short_description',
        'description',
        'category',
        'time_duration',
        'published_on',
        'is_draft',
        'is_deleted',
        'author'
    ]
admin.site.register(Post)
