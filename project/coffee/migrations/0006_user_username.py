# Generated by Django 4.1 on 2022-09-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
