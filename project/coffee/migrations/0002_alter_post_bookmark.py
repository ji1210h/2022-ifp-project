# Generated by Django 4.1 on 2022-08-25 17:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookmark',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]