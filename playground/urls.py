from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_world),
    path("home/", views.front_page),
    path("about/", views.say_hello)
]
