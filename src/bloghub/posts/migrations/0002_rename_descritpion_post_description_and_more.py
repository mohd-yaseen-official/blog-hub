# Generated by Django 5.0.6 on 2024-06-23 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descritpion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='short_descritpion',
            new_name='short_description',
        ),
    ]
