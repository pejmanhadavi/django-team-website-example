from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Local apps urls
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    path('portfolio/', include('apps.portfolio.urls')),
    path('videos/', include('apps.video.urls')),
]

# Set media files as static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
