# Generated by Django 3.1.1 on 2020-10-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20201004_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='bio',
            field=models.CharField(default='', max_length=250),
        ),
    ]