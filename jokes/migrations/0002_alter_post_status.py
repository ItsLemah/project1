# Generated by Django 4.2.4 on 2023-09-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[(0, 'draft'), (1, 'Published')], default=0, max_length=10),
        ),
    ]
