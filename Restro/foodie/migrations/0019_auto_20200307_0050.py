# Generated by Django 3.0.2 on 2020-03-06 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0018_auto_20200307_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='orders_id',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=34, on_delete=django.db.models.deletion.CASCADE, to='foodie.Order'),
            preserve_default=False,
        ),
    ]
