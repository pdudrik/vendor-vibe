from django.urls import path
from . import views


app_name = "core"


urlpatterns = [
    path("", views.home, name="home"),
    path("vendors/", views.VendorView.as_view(), name="vendors"),
    path("vendors/create/", views.CreateVendorView.as_view(), name="create_vendor"),
    path("vendor/<int:pk>/delete/", views.DeleteVendorView.as_view(), name="delete_vendor"),
    path("vendor/<int:pk>/detail/", views.DetailVendorView.as_view(), name="detail_vendor"),
    path("vendor/<int:pk>/update/", views.UpdateVendorView.as_view(), name="update_vendor"),
    path("vendor/<int:pk>/address/create/", views.CreateVendorAddressView.as_view(), name="create_vendor_address"),
    path("vendor/<int:pk>/contact/create/", views.CreateVendorContactView.as_view(), name="create_vendor_contact"),
    path("address/<int:pk>/delete/", views.DeleteAddressView.as_view(), name="delete_address"),
    path("contact/<int:pk>/delete/", views.DeleteContactView.as_view(), name="delete_contact"),
    path("address/<int:pk>/update/", views.UpdateAddressView.as_view(), name="update_address"),
    path("contact/<int:pk>/update/", views.UpdateContactView.as_view(), name="update_contact"),
]