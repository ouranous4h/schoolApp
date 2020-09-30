from django.urls import include, path
from . import views

app_name = "authenticate"
urlpatterns = [
    path("register", views.register, name = "register"),
    path("", views.login, name = "login"),
    path("logout", views.logout, name = "logout"),
]
