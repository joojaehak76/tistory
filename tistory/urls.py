from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import posts_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts_list),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blogs/', include('blogs.urls')),
    path('users/', include('users.urls'),)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
