# Generated by Django 3.1.2 on 2020-11-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20201110_1359'),
        ('order', '0010_auto_20201126_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_location',
            field=models.ManyToManyField(blank=True, to='location.Location'),
        ),
    ]
