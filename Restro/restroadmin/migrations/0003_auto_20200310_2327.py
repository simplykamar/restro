# Generated by Django 3.0.2 on 2020-03-10 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0020_orderupdate'),
        ('restroadmin', '0002_auto_20200310_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderreceived',
            name='restro_profile',
        ),
        migrations.AddField(
            model_name='orderreceived',
            name='restro',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='foodie.Restro'),
            preserve_default=False,
        ),
    ]
