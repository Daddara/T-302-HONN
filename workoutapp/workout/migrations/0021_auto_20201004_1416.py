# Generated by Django 3.1.1 on 2020-10-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0020_auto_20201004_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='Description',
            field=models.TextField(default='', max_length=350),
        ),
    ]
