from django.urls import path

from .views import index, post_page


app_name = 'web'
urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:id>', post_page, name='post_page'),
]