# Generated by Django 5.0.6 on 2024-08-11 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ManyToManyField(to='blog.city'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.ManyToManyField(to='blog.country'),
        ),
    ]
