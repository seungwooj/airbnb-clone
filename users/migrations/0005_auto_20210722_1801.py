# Generated by Django 3.1 on 2021-07-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210720_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('jpy', 'JPY'), ('krw', 'KRW')], default='krw', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('jp', 'Japanese'), ('kr', 'Korean')], default='kr', max_length=2),
        ),
    ]
