# Generated by Django 2.2.4 on 2019-09-18 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20190918_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersaveproduct',
            name='id_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
