# Generated by Django 4.1.7 on 2023-04-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_service', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='shopcart',
            constraint=models.UniqueConstraint(fields=('artist',), name='unique_artist_cart'),
        ),
    ]
