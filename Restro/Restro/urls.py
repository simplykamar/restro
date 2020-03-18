
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodie/',include('foodie.urls')),
    path('account/',include('account.urls')),
    path('restaurant/',include('restroadmin.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
