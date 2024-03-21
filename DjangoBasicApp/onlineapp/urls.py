
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include ('mainapp.urls')),
    path('', include ('loginreg.urls'))
]

urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
