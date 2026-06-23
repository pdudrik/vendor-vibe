from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView,  \
    DeleteView, DetailView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vendor, Contact, Address
from .forms import CreateVendorForm,                    \
    CreateVendorAddressForm, CreateVendorContactForm


@login_required
def home(request):
    return render(request, "core/home.html")


class VendorView(LoginRequiredMixin, ListView):
    model = Vendor
    template_name = "core/vendors.html"
    context_object_name = "vendors"
    ordering = ["name"]
    paginate_by = 20

    def get_queryset(self):
        user_company = self.request.user.company
        return Vendor.objects.filter(company=user_company)
    

class CreateVendorView(LoginRequiredMixin, CreateView):
    model = Vendor
    template_name = "core/create_vendor.html"
    form_class = CreateVendorForm
    success_url = reverse_lazy("core:vendors")

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class DeleteVendorView(LoginRequiredMixin, DeleteView):
    model = Vendor
    success_url = reverse_lazy("core:vendors")


class DetailVendorView(LoginRequiredMixin, TemplateView):
    template_name = "core/detail_vendor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendor_id = self.kwargs["pk"]
        vendor = Vendor.objects.get(pk=vendor_id, company=self.request.user.company)

        context["vendor"] = vendor
        context["contacts"] = vendor.contacts.all()
        context["addresses"] = vendor.addresses.all()

        return context


class CreateVendorAddressView(LoginRequiredMixin, CreateView):
    model = Address
    template_name = "core/create_vendor_address.html"
    form_class = CreateVendorAddressForm

    def form_valid(self, form):
        vendor_pk = self.kwargs["pk"]
        vendor_obj = Vendor.objects.get(pk=vendor_pk, company=self.request.user.company)
        form.instance.vendor_id = vendor_obj.pk

        return super().form_valid(form)
    
    def get_success_url(self):
        vendor_pk = self.kwargs["pk"]
        return reverse("core:detail_vendor", kwargs={"pk": vendor_pk})


class CreateVendorContactView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = "core/create_vendor_contact.html"
    form_class = CreateVendorContactForm

    def form_valid(self, form):
        vendor_pk = self.kwargs["pk"]
        vendor_obj = Vendor.objects.get(pk=vendor_pk, company=self.request.user.company)
        form.instance.vendor_id = vendor_obj.pk

        return super().form_valid(form)
    
    def get_success_url(self):
        vendor_pk = self.kwargs["pk"]
        return reverse("core:detail_vendor", kwargs={"pk": vendor_pk})
