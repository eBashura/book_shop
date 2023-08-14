# Generated by Django 4.2.3 on 2023-08-14 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0005_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manager.book'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
