# Generated by Django 4.0.6 on 2023-08-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_homepage', models.BooleanField(default=False)),
                ('layout', models.CharField(choices=[('list', 'List'), ('grid', 'Grid')], default=list, max_length=10)),
            ],
        ),
    ]
