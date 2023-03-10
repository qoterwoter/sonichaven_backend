# Generated by Django 4.1.7 on 2023-03-07 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название Альбома')),
                ('image', models.FileField(upload_to='album_images/', verbose_name='Обложка альбома')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['artist'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Имя артиста / группы')),
                ('bio', models.TextField(verbose_name='Описание артиста / группы')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('length', models.PositiveIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_card.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_card.artist')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_card.artist', verbose_name='Исполнитель'),
        ),
    ]
