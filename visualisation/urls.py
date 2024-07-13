from django.urls import path
from visualisation import views

urlpatterns = [
    path("", views.home, name="home"),
]