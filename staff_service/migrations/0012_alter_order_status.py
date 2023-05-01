# Generated by Django 4.1.7 on 2023-05-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_service', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PEND', 'Ожидание подтверждения'), ('CONF', 'Подтверждено'), ('SHIP', 'В работе'), ('DELV', 'Завершен'), ('CANC', 'Отменено')], default='PEND', max_length=4, verbose_name='Статус'),
        ),
    ]
