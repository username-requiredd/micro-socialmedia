# Generated by Django 5.1.1 on 2024-11-09 07:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_post_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked_comments',
            field=models.ManyToManyField(blank=True, related_name='like_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
