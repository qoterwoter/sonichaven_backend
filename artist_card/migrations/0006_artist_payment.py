# Generated by Django 4.1.7 on 2023-05-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_card', '0005_song_playcounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Выплата'),
        ),
    ]
