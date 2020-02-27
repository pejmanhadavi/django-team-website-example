from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from apps.blog.models import Category, Article, Review
from apps.blog.forms import ReviewForm


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'article_list.html'
    paginate_by = 4
    queryset = Article.objects.filter(published=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('name'),
        })
        return context


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_single.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        article = Article.objects.filter(slug=slug, published=True).first()
        context.update({
            'category_list': Category.objects.order_by('name'),
            'review_list': Review.objects.filter(article=article.id, published=True, readed=True),
            'review_form': ReviewForm(initial={'article': self.object.id })
        })
        return context
    
    def get_success_url(self):
        return reverse('article_single', kwargs={'slug': self.object.slug})
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        review = Review()
        review.article = self.object
        review.author = form.cleaned_data['author']
        review.email = form.cleaned_data['email']
        review.review = form.cleaned_data['review']
        review.save()
        messages.success(self.request, _('Your review submited successfuly!'))
        return super(ArticleDetailView, self).form_valid(form)


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
