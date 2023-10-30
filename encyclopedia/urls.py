from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.get_entry_by_title, name="get_entry_by_title"),
    path("wiki/<title>/edit", views.edit_entry_by_title, name="edit_entry"),
    path("random", views.get_random, name="random"),
    path("create", views.get_create_form, name="create_entity")
]
