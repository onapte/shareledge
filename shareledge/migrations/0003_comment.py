# Generated by Django 3.2.6 on 2021-11-04 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shareledge', '0002_article_contentimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=2000)),
                ('datePosted', models.CharField(max_length=20)),
                ('timePosted', models.CharField(max_length=20)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='on', to='shareledge.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
