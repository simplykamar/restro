# Generated by Django 3.0.2 on 2020-03-06 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200221_1222'),
        ('foodie', '0017_auto_20200307_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, default=3, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_id',
            field=models.IntegerField(default=42),
            preserve_default=False,
        ),
    ]
