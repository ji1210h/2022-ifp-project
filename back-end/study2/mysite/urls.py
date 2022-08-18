from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    # shkim
    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),
    path('api2/', include('api2.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)