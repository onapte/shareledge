# Generated by Django 3.2.6 on 2021-11-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareledge', '0009_userguidepoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(null=True),
        ),
    ]
