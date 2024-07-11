# Generated by Django 3.0 on 2023-09-09 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RaceApp', '0008_auto_20230909_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anm', models.IntegerField()),
                ('aname', models.CharField(max_length=50)),
                ('aclass', models.CharField(choices=[('0', '----- Select class -----'), ('1', '1st class'), ('2', '2nd class'), ('3', '3rd class'), ('4', '4th class'), ('5', '5th class'), ('6', '6th class'), ('7', '7th class'), ('8', '8th class'), ('9', '9th class'), ('10', '10th class')], default='0', max_length=12)),
                ('asubject', models.CharField(choices=[('J', '---select the subject---'), ('MATHS', 'mathamatics'), ('PHY', 'physics'), ('BIO', 'Biology'), ('SC', 'Social'), ('ENG', 'English'), ('HND', 'Hindi')], default='j', max_length=10)),
                ('adesc', models.CharField(max_length=250)),
                ('astartdate', models.DateField()),
                ('aenddate', models.DateField()),
                ('amarks', models.IntegerField(default=10)),
                ('astatus', models.BooleanField(default=0)),
                ('atch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
