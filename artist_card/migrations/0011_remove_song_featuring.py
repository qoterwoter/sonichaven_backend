# Generated by Django 4.1.7 on 2023-05-06 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist_card', '0010_remove_artist_featuring_song_featuring'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='featuring',
        ),
    ]