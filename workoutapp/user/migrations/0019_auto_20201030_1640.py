# Generated by Django 3.1.1 on 2020-10-30 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20201030_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
