from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # se va a utilizar la autenticacion, por ello se agrega al path
    path('api-auth/', include('rest_framework.urls')) 
]

# se llaman a las urls de 'rest_framework'
if settings.DEGUB:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT
    )












