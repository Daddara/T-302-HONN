# Generated by Django 3.0.6 on 2020-10-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_auto_20201031_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(default=None, null=True),
        ),
    ]