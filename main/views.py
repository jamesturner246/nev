"""Views for the main app."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def map_view(request: HttpRequest) -> HttpResponse:
    """Render the map view."""
    return render(request, "main/base.html")
