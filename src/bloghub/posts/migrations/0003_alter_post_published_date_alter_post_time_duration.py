# Generated by Django 5.0.6 on 2024-06-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_descritpion_post_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_duration',
            field=models.CharField(max_length=1),
        ),
    ]
