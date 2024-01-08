# Generated by Django 4.1.5 on 2023-02-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_concerts_concert_rename_musicians_musician_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='mail',
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
