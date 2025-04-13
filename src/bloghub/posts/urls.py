from django.urls import path

from .views import create_post, my_posts, delete_post, draft_or_publish, edit_post


app_name = 'posts'

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('my-posts/', my_posts, name="my_posts"),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('edit/<int:pk>/', edit_post, name='edit_post'),
    path('draft-or-publish/<int:pk>/', draft_or_publish, name='draft_or_publish'),
]