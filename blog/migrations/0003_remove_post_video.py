# Generated by Django 4.2.4 on 2023-08-27 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]