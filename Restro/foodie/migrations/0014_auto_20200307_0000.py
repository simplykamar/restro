# Generated by Django 3.0.2 on 2020-03-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0013_auto_20200304_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='foodie.OrderItem'),
            preserve_default=False,
        ),
    ]
