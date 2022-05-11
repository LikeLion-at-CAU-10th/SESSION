from . import views
from django.urls import path

urlpatterns = [
    path("", views.footprint_GET),
    path("send", views.footprint_POST),
]
