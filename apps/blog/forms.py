from django import forms

from apps.blog.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('article', 'email', 'author', 'review')
        exclude = ('article',)