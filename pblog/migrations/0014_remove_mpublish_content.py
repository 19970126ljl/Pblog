# Generated by Django 2.1.7 on 2019-03-30 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pblog', '0013_mpublish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mpublish',
            name='content',
        ),
    ]
