# Generated by Django 3.1 on 2020-08-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Title_tag',
            field=models.CharField(default='MY AWSOME BLOGS', max_length=200),
        ),
    ]
