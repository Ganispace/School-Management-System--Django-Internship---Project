# Generated by Django 3.0 on 2023-09-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RaceApp', '0004_auto_20230903_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='semail',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]