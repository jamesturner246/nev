"""URL configuration for the main app."""

from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("map/", views.map_view, name="map_view")
]
