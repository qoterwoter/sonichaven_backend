# Generated by Django 4.1.7 on 2023-03-15 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_service', '0004_sounddesigner_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sounddesigner',
            name='user',
        ),
    ]
