# Generated by Django 3.1.4 on 2021-11-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20211112_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(default=400),
        ),
    ]
