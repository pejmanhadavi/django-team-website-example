from django.views.generic import ListView

from apps.blog.models import Category, Article, Review


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'article_list.html'