# Generated by Django 3.0.2 on 2020-03-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0008_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
