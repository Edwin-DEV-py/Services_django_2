# Generated by Django 4.2.2 on 2023-07-21 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postID', models.IntegerField()),
                ('content', models.TextField(max_length=300)),
            ],
        ),
    ]
