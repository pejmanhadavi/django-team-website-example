from django.urls import path
from django.views.generic import TemplateView

from apps.blog.views import ArticleListView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('single/', TemplateView.as_view(template_name='article_single.html'), name='article_single'),
    path('category/', TemplateView.as_view(template_name='article_list.html'), name='article_category')
]
