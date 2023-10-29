from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.get_entry_by_title, name="get_entry_by_title"),
    path("random", views.get_random, name="random")
]
