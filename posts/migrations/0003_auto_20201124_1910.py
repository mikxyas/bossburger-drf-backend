# Generated by Django 3.1.2 on 2020-11-24 16:10

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_path),
        ),
    ]