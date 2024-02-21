from . import views
from django.urls import path

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("main", views.main, name="main"),
    path("path", views.path, name="path"),

]
