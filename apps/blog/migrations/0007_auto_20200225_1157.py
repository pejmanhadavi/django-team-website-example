# Generated by Django 3.0.3 on 2020-02-25 11:57

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200225_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]