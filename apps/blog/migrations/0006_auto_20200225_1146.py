# Generated by Django 3.0.3 on 2020-02-25 11:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200224_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
