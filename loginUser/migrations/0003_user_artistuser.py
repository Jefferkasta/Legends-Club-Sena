# Generated by Django 5.0 on 2023-12-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginUser', '0002_user_identificationuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='artistUser',
            field=models.BooleanField(default=False),
        ),
    ]