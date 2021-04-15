from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search_results", views.search, name="search_results"),
    path("search", views.search, name="search"),
    path("<str:title>", views.title, name="title"),

]
