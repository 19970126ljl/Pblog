# Generated by Django 2.1.7 on 2019-03-28 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pblog', '0004_auto_20190328_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marticle',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_writer', to='pblog.MUSER'),
        ),
    ]
