# Generated by Django 3.0 on 2023-09-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RaceApp', '0005_studentprofile_semail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='tdesg',
            field=models.CharField(max_length=50),
        ),
    ]