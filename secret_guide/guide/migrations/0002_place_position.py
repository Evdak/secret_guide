# Generated by Django 4.2.2 on 2023-09-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='position',
            field=models.PositiveIntegerField(default=100, verbose_name='Позиция на сайте'),
        ),
    ]
