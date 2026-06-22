from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
# from .models import Vendor


@login_required
def home(request):
    return render(request, "core/home.html")


# class VendorView(ListView):
#     model = Vendor

class VendorView(TemplateView):
    template_name = "core/vendors.html"
