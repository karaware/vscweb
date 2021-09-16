from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('njiro/', include('vscwebnjiro.urls')),
    path('pekora/', include('vscwebpekora.urls')),
    path('tomeru/', include('vscwebtomeru.urls')),
]
