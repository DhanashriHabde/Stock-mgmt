# Generated by Django 3.2 on 2021-08-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
    ]