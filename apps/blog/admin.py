from django.contrib import admin
from apps.blog import models


admin.site.register(models.Category)
admin.site.register(models.Article)
admin.site.register(models.Review)
