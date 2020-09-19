# Generated by Django 3.1.1 on 2020-09-11 12:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout', '0002_auto_20200911_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='Public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='exercise',
            unique_together={('Creator', 'Title')},
        ),
    ]