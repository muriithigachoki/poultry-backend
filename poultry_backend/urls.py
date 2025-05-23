from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("account.apis.urls")),
    path("api/", include("products.apis.urls")),
    path("api/day-old-chicks/", include("old_day_chicks.apis.urls")),
    path("api/payments/", include("mpesa.apis.urls")),
    path("api/farm/", include("farm.apis.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "Kangai poultry management system site admin (DEV)"
admin.site.site_header = "Kangai poultry management system administration"
admin.site.index_title = "Site administration"
