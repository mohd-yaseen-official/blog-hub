import csv
from os import name
import random
import uuid

import wget

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from posts.models import Author, Category, Post


class Command(BaseCommand):
    help = 'This command creates a new blog post'
    def handle(self, *args, **options):
        print('Deleting data..........')

        Category.objects.all().delete()
        print("""  Deleted Categories""")
        Post.objects.all().delete()
        print("""  Deleted Posts""")
        Author.objects.all().delete()
        print("""  Deleted Authors""")

        print("""
              All fields Cleared""")
        
        file = open(settings.BASE_DIR / "new_posts.csv", encoding='utf-8')

        csv_reader = csv.reader(file)

        next(csv_reader)

        for row in csv_reader:
            author_name  = row[1].split(",")[0]
            content = row[2]
            date = row[3]
            img_srcs = row[4]
            tags = row[5]
            title = row[6]

            file_name = f'{uuid.uuid4()}.jpg'
            file_path = f'{settings.BASE_DIR}/media/posts/{file_name}'

            image_filename = wget.download(img_srcs, file_path)

            uploaded_file_url = f'posts/{file_name}'

            if Author.objects.filter(name=author_name).exists():
                author = Author.objects.filter(name=author_name)[0]
            else:
                user = User.objects.create_user(
                    username=uuid.uuid4(),
                    password='password',
                    first_name=author_name
                )

                author = Author.objects.create(
                    name=author_name,
                    user=user
                )

            post = Post.objects.create(
                title=title,
                short_description=" ".join(content.split(" ")[:25]),
                description=content,
                time_duration=f"{random.randint(0, 11)} min",

                featured_image = uploaded_file_url,

                author=author,
                published_date=date

            )

            tags_list = tags.split(",")
            for tag in tags_list:
                if not tag.strip() == "":
                    item, created = Category.objects.get_or_create(title=tag)

                    post.categories.add(item)

        print("Proccess Completed......Success!")