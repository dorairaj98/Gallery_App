from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from gallery import settings
from gallery_app import views as user_view

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('gallery_app.urls')),
    path('upload/', user_view.index, name='dashboard'),
    path('project_detail/', user_view.gallerylist.as_view(), name='gallerylist' ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
