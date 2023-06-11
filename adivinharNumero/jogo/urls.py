from django.urls import path

from . import views

urlpatterns = [
    path("<str:usuario>/atrio/", views.atrio, name="atrio"),
    path("<int:id_ns>/", views.jogo, name="jogo"),
    path("check/<int:id_ns>/", views.check, name="check"),
]