# Generated by Django 3.0.3 on 2020-02-24 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=128, verbose_name='slug')),
                ('image', models.ImageField(blank=True, upload_to='articles/images/')),
                ('description', models.TextField(max_length=256, verbose_name='description')),
                ('body', models.TextField(verbose_name='body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=128, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name', 'slug'], name='category_index'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.Category', verbose_name='category'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['title', 'slug', 'description', 'image', 'updated_at', 'author', 'category'], name='article_index'),
        ),
    ]