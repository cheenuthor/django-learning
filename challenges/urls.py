from django.urls import path

from . import views

# created url config
urlpatterns = [
    path("january", views.january),
    path("february", views.february)
]
