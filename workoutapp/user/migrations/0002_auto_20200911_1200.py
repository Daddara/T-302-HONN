# Generated by Django 3.1.1 on 2020-09-11 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='SenderDate',
        ),
        migrations.AddField(
            model_name='messages',
            name='SendDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Messages',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Seen',
            field=models.BooleanField(default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='BirthYear',
            field=models.DateTimeField(default=datetime.date(2020, 9, 11)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='CreatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='FirstName',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Image',
            field=models.CharField(default='https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png', max_length=250),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='LastName',
            field=models.CharField(default='', max_length=20),
        ),
    ]
