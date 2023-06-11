from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("login/check/", views.valida_usuario, name="valida_usuario"),
    path("register/check", views.registra_usuario, name="registra_usuario"),
]