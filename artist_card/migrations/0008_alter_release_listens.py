# Generated by Django 4.1.7 on 2023-05-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_card', '0007_release_listens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='listens',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество прослушиваний'),
        ),
    ]
