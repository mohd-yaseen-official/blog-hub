from django.db import models

from ckeditor.fields import RichTextField


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.title
    

class Post(models.Model):

    title = models.CharField(max_length=255)
    short_description = models.TextField()

    description = RichTextField()
    categories = models.ManyToManyField("posts.Category")

    time_duration = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to='posts')

    author = models.ForeignKey("posts.Author", on_delete=models.CASCADE)
    published_date = models.DateField()

    is_draft = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title





    
