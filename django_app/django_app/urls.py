from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", include("hello.urls")),
    path('sns/', include('sns.urls')),
    path('accounts/',include('accounts.urls')),

]

# 以下を定義
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)