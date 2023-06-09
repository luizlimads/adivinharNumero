from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("check/", views.valida_usuario, name="valida_usuario"),
]