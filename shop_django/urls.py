from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from account.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("account.urls")),
    path("account/", include("account.urls")),
]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
