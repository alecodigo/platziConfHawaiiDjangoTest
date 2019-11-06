"""platziConfHawaii URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('platzi-conf-hawaii/', include(('speaker.urls', 'speaker'), namespace='speaker')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static(settings....) is not suitable for production use Ok!
