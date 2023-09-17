from django.urls import path
from authapp import views

urlpatterns = [
    path("signup/", views.handlesignup,name="handlesignup"),
    path("login/", views.handlelogin,name="handlelogin"),
    path("logout/", views.handleLogout,name="handleLogout"),


]