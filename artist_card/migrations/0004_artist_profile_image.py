# Generated by Django 4.1.7 on 2023-04-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_card', '0003_remove_song_featured_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile_image',
            field=models.CharField(default=1, max_length=255, verbose_name='Аватар'),
            preserve_default=False,
        ),
    ]