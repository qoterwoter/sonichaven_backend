# Generated by Django 4.1.7 on 2023-05-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_service', '0008_remove_orderitem_sum_order_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Confirmed'), ('S', 'Shipped'), ('D', 'Delivered'), ('X', 'Cancelled')], default='P', max_length=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Оформлен'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма'),
        ),
    ]
