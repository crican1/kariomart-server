# Generated by Django 4.2.1 on 2023-08-01 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kariomartapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='image_url',
            field=models.CharField(default=1, max_length=1000),
        ),
    ]
