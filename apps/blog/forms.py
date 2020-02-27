from django import forms
from django.utils.translation import gettext_lazy as _

from captcha.fields import CaptchaField

from apps.blog.models import Review


class ReviewForm(forms.ModelForm):
    captcha = CaptchaField(label=_("Captcha"))
    class Meta:
        model = Review
        fields = ('author', 'email', 'review')