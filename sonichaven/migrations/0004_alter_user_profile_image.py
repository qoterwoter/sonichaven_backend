# Generated by Django 4.1.7 on 2023-05-30 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sonichaven', '0003_user_phonenumber_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='Фотография профиля'),
        ),
    ]
