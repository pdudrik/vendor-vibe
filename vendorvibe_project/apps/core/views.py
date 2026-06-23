from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView,  \
    DeleteView, DetailView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vendor, Contact, Address
from .forms import CreateVendorForm,                    \
    CreateVendorAddressForm, CreateVendorContactForm
from .mixin import CompanyDataMixin


@login_required
def home(request):
    return render(request, "core/home.html")


class VendorView(LoginRequiredMixin, CompanyDataMixin, ListView):
    model = Vendor
    template_name = "core/vendors.html"
    context_object_name = "vendors"
    ordering = ["name"]
    paginate_by = 20
    

class CreateVendorView(LoginRequiredMixin, CompanyDataMixin, CreateView):
    model = Vendor
    template_name = "core/create_vendor.html"
    form_class = CreateVendorForm
    success_url = reverse_lazy("core:vendors")


class DeleteVendorView(LoginRequiredMixin, CompanyDataMixin, DeleteView):
    model = Vendor
    success_url = reverse_lazy("core:vendors")


class DetailVendorView(LoginRequiredMixin, CompanyDataMixin, DetailView):
    model = Vendor
    template_name = "core/detail_vendor.html"
    context_object_name = "vendor"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["contacts"] = self.object.contacts.all()
        context["addresses"] = self.object.addresses.all()

        return context


class CreateVendorAddressView(LoginRequiredMixin, CompanyDataMixin, CreateView):
    model = Address
    template_name = "core/create_vendor_address.html"
    form_class = CreateVendorAddressForm
    
    def get_success_url(self):
        vendor_pk = self.kwargs["pk"]
        return reverse("core:detail_vendor", kwargs={"pk": vendor_pk})


class DeleteVendorAddressView(LoginRequiredMixin, DeleteView):
    pass

class DeleteVendorContactView(LoginRequiredMixin, DeleteView):
    pass


class CreateVendorContactView(LoginRequiredMixin, CompanyDataMixin, CreateView):
    model = Contact
    template_name = "core/create_vendor_contact.html"
    form_class = CreateVendorContactForm
    
    def get_success_url(self):
        vendor_pk = self.kwargs["pk"]
        return reverse("core:detail_vendor", kwargs={"pk": vendor_pk})
