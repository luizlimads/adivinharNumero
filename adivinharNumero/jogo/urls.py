from django.urls import path

from . import views

urlpatterns = [
    path("<str:usuario>/atrio/", views.redireciona_atrio, name="atrio"),
    path("<str:usuario>/atrio/1/", views.atrio_1, name="atrio_1"),
    path("<str:usuario>/atrio/2/", views.atrio_2, name="atrio_2"),
    
    path("<str:usuario>/jogo/", views.redireciona_jogo, name="jogo"),
    path("<str:usuario>/jogo/1/", views.jogo_1, name="jogo_1"),
    #path("<str:usuario>/jogo/2/", views.atrio_2, name="atrio_2"),


    path("<int:id_ns>/", views.jogo, name="jogo"),
    path("check/<int:id_ns>/", views.check, name="check"),
]