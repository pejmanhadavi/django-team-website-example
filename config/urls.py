import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    # Admin urls
    path('admin/', admin.site.urls),
    
    # ckeditor urls
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Local apps urls
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    path('portfolio/', include('apps.portfolio.urls')),
    path('videos/', include('apps.video.urls')),
]

# Set media files as static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# captcha
urlpatterns += [
    path('captcha/', include('captcha.urls')),
]

# Set debug toolbar in debug mode
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [ path('__debug__/', include(debug_toolbar.urls)) ] + urlpatterns
