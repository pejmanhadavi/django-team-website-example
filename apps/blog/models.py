from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from ckeditor_uploader.fields import RichTextUploadingField
from image_cropping import ImageRatioField


class Category(models.Model):
    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name=_('title'))
    slug = models.SlugField(
        max_length=128,
        blank=False,
        null=False,
        allow_unicode=True,
        verbose_name=_('slug'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        indexes = [
            models.Index(fields=['name', 'slug'], name='category_index'),
        ]
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_category', kwargs={'slug': self.slug})


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

    image = models.ImageField(
        upload_to='articles/images/',
        blank=True)
    cropping = ImageRatioField('image', '750x300')
    description = models.TextField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name=_('description'))
    # body = models.TextField(
    
    body = RichTextUploadingField(
        blank=False,
        null=False,
        verbose_name=_('body'))
    published = models.BooleanField(
        default=False,
        null=False,
        verbose_name=_('published'))
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

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        indexes = [
            models.Index(
                fields=[
                    'title',
                    'slug',
                    'description',
                    'image',
                    'updated_at',
                    'author',
                    'category'
                ],
                name='article_index'),
        ]
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_single', kwargs={'slug': self.slug})


class Review(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=False,
        null=False,
        verbose_name=_('article'))
    email = models.EmailField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name=_('email'))
    author = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name=_('author'))
    review = models.CharField(
        max_length=512,
        blank=False,
        null=False,
        verbose_name=_('review'))
    reply_to = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='reviews',
        verbose_name=_('reply'))
    created_at = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True,
        verbose_name=_('created at'))
    published = models.BooleanField(
        default=False,
        null=False,
        verbose_name=_('published'))
    readed = models.BooleanField(
        default=False,
        null=False,
        verbose_name=_('readed'))

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
        ordering = ['-created_at']

    def __str__(self):
        return self.review
