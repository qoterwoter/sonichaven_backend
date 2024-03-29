# Generated by Django 4.1.7 on 2023-05-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_card', '0014_alter_release_options_remove_release_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='status',
            field=models.CharField(choices=[('released', 'Released'), ('awaiting_upload', 'Awaiting upload'), ('archived', 'Archived'), ('in_progress', 'In progress')], default='in_progress', max_length=20, verbose_name='Status'),
        ),
    ]
