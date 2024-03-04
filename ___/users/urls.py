from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("account/", views.account, name="account"),
    path("account/edit", views.edit, name="edit"),
]
