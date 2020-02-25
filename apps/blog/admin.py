from django.contrib import admin
from apps.blog.models import Category, Article, Review

from image_cropping import ImageCroppingMixin


class ReviewInline(admin.TabularInline):
    model = Review
    list_per_page = 10
    readonly_fields = ('created_at', 'reply_to', 'author', 'email', 'article',)
    extra = 1


@admin.register(Article)
class ArticleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [
        ReviewInline
    ]
    list_display = ('id', 'title', 'published', 'author', 'updated_at', 'created_at',)
    list_display_links = ('id', 'title',)
    list_filter = ('title', 'slug', 'author',)
    list_editable = ('published',)
    search_fields = ('title', 'description', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 15


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug')
    list_display_links = ('id', 'name', 'slug')
    list_filter = ('name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 15