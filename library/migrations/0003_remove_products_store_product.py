# Generated by Django 2.2.4 on 2019-09-04 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190903_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='store_product',
        ),
    ]
