# Generated by Django 4.1.7 on 2023-04-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_service', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='items',
            field=models.ManyToManyField(to='staff_service.cartitem', verbose_name='Предмет заказа'),
        ),
    ]