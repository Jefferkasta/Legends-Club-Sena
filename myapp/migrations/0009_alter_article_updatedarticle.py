# Generated by Django 5.0 on 2023-12-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_article_imagearticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updatedArticle',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
