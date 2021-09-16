# Generated by Django 3.2.7 on 2021-09-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoId', models.TextField(max_length=255)),
                ('videoTitle', models.TextField(max_length=255)),
                ('startTime', models.TextField(max_length=255)),
                ('endTime', models.TextField(max_length=255)),
                ('likeCount', models.IntegerField()),
                ('maxViewers', models.IntegerField()),
                ('videoUrl', models.TextField(max_length=255)),
                ('s3ThumbnailUrl', models.TextField(max_length=255)),
                ('s3GraphUrl', models.TextField(max_length=255)),
            ],
        ),
    ]