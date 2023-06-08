from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path("jogo/", include("jogo.urls")),
    path('admin/', admin.site.urls),
]
