# Generated by Django 3.2.6 on 2021-11-05 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareledge', '0004_article_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
