from django import forms

from captcha.fields import CaptchaField

from apps.blog.models import Review


class ReviewForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Review
        fields = ('author', 'email', 'review')