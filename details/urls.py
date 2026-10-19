from django.urls import path
from . import views

urlpatterns = [
    path("", views.details_form, name="details_form"),
]