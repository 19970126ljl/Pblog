# Generated by Django 2.1.7 on 2019-03-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='gender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='muser',
            name='types',
            field=models.BooleanField(default=False),
        ),
    ]
