# Generated by Django 3.0 on 2023-09-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RaceApp', '0010_attendance_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maths', models.IntegerField(default=50)),
                ('hindi', models.IntegerField(default=50)),
                ('eng', models.IntegerField(default=50)),
                ('phy', models.IntegerField(default=50)),
                ('biology', models.IntegerField(default=50)),
                ('social', models.IntegerField(default=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]