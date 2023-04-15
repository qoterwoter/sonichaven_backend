# Generated by Django 4.1.7 on 2023-04-14 21:09

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
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('author', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.CharField(blank=True, max_length=255, null=True, verbose_name='Изображение')),
                ('caption', models.CharField(blank=True, max_length=100, verbose_name='Описание изображения')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='news_blog.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Абзац',
                'verbose_name_plural': 'Абзацы',
                'ordering': ['id'],
            },
        ),
    ]
