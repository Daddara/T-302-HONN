# Generated by Django 3.1.1 on 2020-11-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0025_exercise_has_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='has_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
