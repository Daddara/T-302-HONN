# Generated by Django 3.1.1 on 2020-10-03 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0017_workout_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='workout_goal',
            field=models.CharField(default='', max_length=80),
        ),
    ]
