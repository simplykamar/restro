# Generated by Django 3.0.2 on 2020-02-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0002_auto_20200211_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restro',
            name='discount',
            field=models.IntegerField(blank=True, choices=[(30, '30%'), (40, '40%'), (50, '50%'), (60, '60%')]),
        ),
    ]
