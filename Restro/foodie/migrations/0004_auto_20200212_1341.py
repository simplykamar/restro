# Generated by Django 3.0.2 on 2020-02-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0003_auto_20200212_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restro',
            name='discount',
            field=models.IntegerField(blank=True, choices=[(30, '30%'), (40, '40%'), (50, '50%'), (60, '60%')], null=True),
        ),
    ]
