# Generated by Django 2.1.7 on 2019-03-31 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pblog', '0021_auto_20190331_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpublish',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]