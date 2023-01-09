"""URLs for the djv_example app."""
from django.urls import path

from . import views


urlpatterns = [
    path('',
        views.WelcomeAppView.as_view(),
        name='djv_example_default'),
]
