# Generated by Django 3.1.1 on 2020-10-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0010_auto_20200930_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='Repetitions',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
