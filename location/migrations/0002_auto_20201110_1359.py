# Generated by Django 3.1.2 on 2020-11-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='cords',
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.CharField(default='lat', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='locDistance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='locPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.CharField(default='long', max_length=100),
            preserve_default=False,
        ),
    ]