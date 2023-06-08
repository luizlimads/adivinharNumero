from django.urls import path

from . import views

urlpatterns = [
    path("<int:id_ns>/", views.index, name="index"),
    path("check/<int:id_ns>/", views.check, name="check"),

]