# Generated by Django 2.1.7 on 2019-03-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pblog', '0007_mcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marticle',
            name='content',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='marticle',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mcomment',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]