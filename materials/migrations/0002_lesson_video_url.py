# Generated by Django 5.0.6 on 2024-05-10 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='ссыока на видео'),
        ),
    ]