# Generated by Django 3.1.1 on 2020-10-04 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0018_workout_workout_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='CreatedAt',
        ),
    ]
