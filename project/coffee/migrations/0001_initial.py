# Generated by Django 4.1 on 2022-10-20 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('profile_image', models.ImageField(default='profile/2022/10/default.png', upload_to='profile/%Y/%m')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('image', models.ImageField(default='coffee/2022/10/default.png', upload_to='coffee/%Y/%m', verbose_name='IMAGE')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='UPDATE DT')),
                ('bookmark_user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee.category')),
                ('material', models.ManyToManyField(to='coffee.material')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('update_dt',),
            },
        ),
    ]
