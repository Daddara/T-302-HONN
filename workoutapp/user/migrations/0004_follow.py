# Generated by Django 3.1.1 on 2020-09-20 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_auto_20200911_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FollowedAt', models.DateTimeField(auto_now=True)),
                ('Following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Following', to=settings.AUTH_USER_MODEL)),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Username', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]