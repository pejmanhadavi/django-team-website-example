from django.urls import path
from django.views.generic import TemplateView

from apps.blog.views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_single'),
    path('category/<slug:slug>/', TemplateView.as_view(template_name='article_list.html'), name='article_category')
]
