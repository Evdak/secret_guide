from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from kstati import urls as kstati_urls
from quests import urls as quests_urls
from guide import urls as guide_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('kstati/', include(kstati_urls)),
    path('quest/', include(quests_urls)),
    path('guide/', include(guide_urls)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
