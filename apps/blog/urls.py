from django.urls import path
from django.views.generic import TemplateView

from apps.blog.views import ArticleListView, ArticleDetailView, ArticleCategoryView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_single'),
    path('category/<slug:slug>/', ArticleCategoryView.as_view(), name='article_category')
]
