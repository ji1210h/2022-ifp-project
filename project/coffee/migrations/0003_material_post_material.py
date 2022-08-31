# Generated by Django 4.1 on 2022-08-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_alter_post_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='material',
            field=models.ManyToManyField(to='coffee.material'),
        ),
    ]