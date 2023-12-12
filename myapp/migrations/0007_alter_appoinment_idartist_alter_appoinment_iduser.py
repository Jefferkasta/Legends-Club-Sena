# Generated by Django 5.0 on 2023-12-09 21:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_appoinment_updatedappointment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='idArtist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artist'),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]