# Generated by Django 4.2.3 on 2023-08-16 13:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0007_book_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(related_name='liked_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
