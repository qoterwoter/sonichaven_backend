# Generated by Django 4.1.7 on 2023-04-14 21:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist_card', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость')),
                ('type', models.CharField(choices=[('Exclusive', 'Эксклюзив'), ('Leasing', 'Базовый лизинг'), ('Leasing+', 'Коммерческий лизинг'), ('Key', 'Под ключ'), ('Production', 'Продакшн музыка'), ('Mixing', 'Сведение'), ('Mixing+', 'Сведение и Мастеринг'), ('Distribution', 'Дистрибуция')], max_length=12, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='SoundEngineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('nickname', models.CharField(max_length=50, unique=True, verbose_name='Псеводним')),
                ('sex', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский'), ('O', 'Другой')], max_length=1, verbose_name='Пол')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Баланс')),
                ('services', models.ManyToManyField(to='staff_service.service', verbose_name='Услуги')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sounddesigner_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Звукоржессер',
                'verbose_name_plural': 'Звукоржессеры',
            },
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма заказа')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='artist_card.artist', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enjoy_date', models.DateField(verbose_name='Дата вступления в компанию')),
                ('payment', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Заработная плата')),
                ('user', models.OneToOneField(limit_choices_to={'is_staff': True, 'is_superuser': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_terms', models.TextField(verbose_name='Условия контракта')),
                ('signing_date', models.DateField(verbose_name='Дата подписания')),
                ('duration', models.PositiveIntegerField(help_text='Длительность контракта в месяцах', verbose_name='Длительность')),
                ('artist_signed', models.BooleanField(default=False, verbose_name='Подпись артиста')),
                ('studio_admin_signed', models.BooleanField(default=False, verbose_name='Подпись администратора')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist_card.artist', verbose_name='Артист')),
            ],
            options={
                'verbose_name': 'Контракт',
                'verbose_name_plural': 'Контракты',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='staff_service.shopcart')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff_service.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Позиция в корзине',
                'verbose_name_plural': 'Позиции в корзине',
            },
        ),
        migrations.CreateModel(
            name='Arrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('duration', models.DurationField(default=datetime.timedelta(0), verbose_name='Длительность')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость (RUB)')),
                ('format', models.CharField(choices=[('wav', 'WAV'), ('mp3', 'MP3'), ('flac', 'FLAC'), ('aac', 'AAC'), ('dsd', 'DSD')], max_length=4, verbose_name='Формат')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrangements', to='staff_service.sounddesigner', verbose_name='Автор')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrangements', to='staff_service.genre')),
            ],
            options={
                'verbose_name': 'Арранжировка',
                'verbose_name_plural': 'Арранжировки',
            },
        ),
    ]
