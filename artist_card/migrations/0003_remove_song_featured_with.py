# Generated by Django 4.1.7 on 2023-04-15 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist_card', '0002_song_featured_with'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='featured_with',
        ),
    ]