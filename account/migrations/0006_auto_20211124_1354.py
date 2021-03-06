# Generated by Django 3.2.2 on 2021-11-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_booking_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeservicer',
            name='availability_status',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], default='available', max_length=50),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='availability_status',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], default='available', max_length=50),
        ),
    ]
