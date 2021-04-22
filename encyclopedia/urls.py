from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random_page", views.random_page, name="random_page"),
    path("wiki/new_page", views.new_page, name="new_page"),
    path("search_results", views.search, name="search_results"),
    path("search", views.search, name="search"),
    path("wiki/<title>", views.title, name="title"),
    path("wiki/<title>/edit", views.edit_page, name="edit_page"),

]
