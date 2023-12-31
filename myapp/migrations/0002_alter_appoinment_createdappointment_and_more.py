# Generated by Django 4.2.7 on 2023-12-03 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='createdAppointment',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='article',
            name='createdArticle',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='artist',
            name='createdArtist',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='artist',
            name='updatedArtist',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
