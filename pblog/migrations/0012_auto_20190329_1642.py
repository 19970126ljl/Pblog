# Generated by Django 2.1.7 on 2019-03-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pblog', '0011_auto_20190329_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malbum',
            name='ctime',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mphoto',
            name='ctime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
