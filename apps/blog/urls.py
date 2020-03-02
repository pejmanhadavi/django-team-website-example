from django.urls import path
from django.views.generic import TemplateView

from apps.blog.views import ArticleListView, ArticleDetailView, ArticleCategoryView, ArticleSearchView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('search/', ArticleSearchView.as_view(), name='article_search'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_single'),
    path('category/<slug:slug>/', ArticleCategoryView.as_view(), name='article_category'),
]
