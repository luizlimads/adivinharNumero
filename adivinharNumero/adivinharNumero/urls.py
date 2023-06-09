from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path("usuario/", include("usuario.urls")),
    path("usuario/", include("jogo.urls")),
    path('admin/', admin.site.urls),
]
