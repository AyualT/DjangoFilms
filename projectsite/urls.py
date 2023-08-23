from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('films.urls')),
    path('studios/',include('studios.urls')),
    path('actors/',include('actors.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('users/',include('users.urls')),
    path('captcha/', include('captcha.urls')),
    path(r'^tracking', include('tracking.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns+=[
        path('__debug__', include('debug_toolbar.urls'))
    ]