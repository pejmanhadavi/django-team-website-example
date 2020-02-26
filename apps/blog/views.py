from django.views.generic import ListView

from apps.blog.models import Category, Article, Review


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'article_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('name'),
        })
        return context
