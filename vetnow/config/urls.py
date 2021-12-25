from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('comment.urls')),
    path('api/v1/', include('order.urls')),
    path('api/v1/', include('threeD.urls')),
    path('api/v1/', include('accounting.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
