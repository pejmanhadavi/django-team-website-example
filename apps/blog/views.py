from django.views.generic import ListView, DetailView

from apps.blog.models import Category, Article, Review


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'article_list.html'
    paginate_by = 4
    queryset = Article.objects.filter(published=True).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('name'),
        })
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_single.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        article = Article.objects.filter(slug=slug, published=True).first()
        context.update({
            'category_list': Category.objects.order_by('name'),
            'review_list': Review.objects.filter(article=article.id, published=True, readed=True)
        })
        return context


class ArticleCategoryView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'article_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(ArticleCategoryView, self).get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('name'),
        })
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = Article.objects.all()
        slug = self.kwargs['slug']
        if slug:
            category = Category.objects.filter(slug=slug).first()
            queryset = queryset.filter(published=True, category=category.id)
        return queryset
