# Generated by Django 4.1.7 on 2023-04-14 21:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя артиста / группы')),
                ('bio', models.TextField(verbose_name='Описание артиста / группы')),
                ('user', models.ForeignKey(limit_choices_to={'is_artist': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.CharField(max_length=255, verbose_name='Обложка')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('type', models.CharField(choices=[('album', 'Альбом'), ('mixtape', 'Микстейп'), ('ep', 'Епи'), ('single', 'Сингл')], max_length=12, verbose_name='Тип релиза')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_card.artist', verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Релиз',
                'verbose_name_plural': 'Релизы',
                'ordering': ['artist'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название песни')),
                ('duration', models.DurationField(default=datetime.timedelta(0), verbose_name='Длительность')),
                ('track_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер песни в релизе')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_card.artist', verbose_name='Исполнитель')),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='artist_card.release', verbose_name='Релиз')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
                'ordering': ['release', 'track_number'],
                'unique_together': {('release', 'track_number')},
            },
        ),
    ]
