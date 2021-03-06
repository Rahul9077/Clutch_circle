# Generated by Django 3.1.4 on 2021-01-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sweets',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('short_desc', models.CharField(default='', max_length=300)),
                ('slug', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
