from django.contrib import admin
from django.urls import path
from final import views

urlpatterns = [
    path("", views.index, name="root"),
    path("about/", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginUser, name="login"),
    path("contact/", views.contact, name="contact"),
    path("logout/", views.logoutUser, name="logout"),
    path("services/", views.services, name="services")
]
