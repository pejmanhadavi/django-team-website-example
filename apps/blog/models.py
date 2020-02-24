from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name=_('title'))
    image = models.ImageField(
        upload_to='articles/images/',
        blank=True)
    slug = models.SlugField(
        max_length=128,
        blank=False,
        null=False,
        allow_unicode=True,
        verbose_name=_('slug'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_category', kwargs={'slug': self.slug})


class Article(models.Model):
    title = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name=_('title'))
    slug = models.SlugField(
        max_length=128,
        blank=False,
        null=False,
        allow_unicode=True,
        verbose_name=_('slug'))
    category = models.ForeignKey(
        Category,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name=_('category'))
    author = models.ForeignKey(
        get_user_model(),
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name=_('author'))
    description = models.TextField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name=_('description'))
    body = models.TextField(
        blank=False,
        null=False,
        verbose_name=_('body'))
    created_at = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True,
        verbose_name=_('created at'))
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        verbose_name=_('updated at'))
