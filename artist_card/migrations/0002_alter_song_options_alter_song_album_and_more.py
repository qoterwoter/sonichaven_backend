# Generated by Django 4.1.7 on 2023-03-07 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist_card', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['artist'], 'verbose_name': 'Песня', 'verbose_name_plural': 'Песни'},
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_card.album', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_card.artist', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название песни'),
        ),
    ]
