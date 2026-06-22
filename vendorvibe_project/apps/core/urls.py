from django.urls import path
from . import views


app_name = "core"


urlpatterns = [
    path("", views.home, name="home"),
    path("vendors/", views.VendorView.as_view(), name="vendors"),
]