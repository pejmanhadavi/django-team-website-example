# Generated by Django 3.0.3 on 2020-02-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200224_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='readed',
            field=models.BooleanField(default=False, verbose_name='readed'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=512, verbose_name='review'),
        ),
    ]
