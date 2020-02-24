from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='blog_list.html'), name='blog_list'),
    path('single/', TemplateView.as_view(template_name='blog_single.html'), name='blog_single'),
]
