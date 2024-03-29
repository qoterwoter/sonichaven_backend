# Generated by Django 4.1.7 on 2023-05-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_service', '0009_order_status_alter_order_created_at_alter_order_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PEND', 'Ожидание'), ('CONF', 'Подтверждено'), ('SHIP', 'Отправлено'), ('DELV', 'Доставлено'), ('CANC', 'Отменено')], default='PEND', max_length=4, verbose_name='Статус'),
        ),
    ]
