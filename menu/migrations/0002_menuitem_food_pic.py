# Generated by Django 3.1.2 on 2020-11-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='food_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
