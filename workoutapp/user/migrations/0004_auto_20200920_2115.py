# Generated by Django 3.1.1 on 2020-09-20 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200911_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='FirstName',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='LastName',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='User',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='BirthYear',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]