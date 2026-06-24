from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .models import Vendor


class CompanyDataMixin:
    """
    Automated security for data isolation.
    Isolate data from users from companies they
    don't have access to.
    """

    def dispatch(self, request, *args, **kwargs):
        # Enforce for user to be authenticated and assigned company workspace
        if not request.user.is_authenticated or not hasattr(request.user, "company") or request.user.company is None:
            raise PermissionDenied("""
                You must belong to an active company workspace.""")
        
        # Authenticated and assigned company workspace
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        # Dynamically assigned model
        queryset = super().get_queryset()
        # Company to which user has permission (assigned workspace)
        user_comapny = self.request.user.company    

        # Check if user accesses company to which he has permission
        # (to which company workspace are they assigned).
        # This if statement checks only those models which have
        # direct relationship to Company model like Vendors.
        if hasattr(queryset.model, "company"):
            # Return all vendors from comapny workspace
            return queryset.filter(company=user_comapny)
        # Check for permission as well but this checks those models
        # which haven't direct relationship with model Company.
        # They are connected through another model
        # e.g. Contact (does not) -> Vendor (does) -> Company.
        elif hasattr(queryset.model, "vendor"):
            # Return all requested records from specified model
            # which are in the company workpace.
            return queryset.filter(vendor__company=user_comapny)
        
        return queryset
    
    def form_valid(self, form):
        # First check if form has instace (collected input fields
        # from frontend form), if not it's delete request from
        # DeleteView for certain model. If so skip injection bellow
        # and allow deleting record.
        # GUARD: Deleting existing record (e.g. DeleteView)
        if not hasattr(form, "instance"):
            return super().form_valid(form)
        
        user_company = self.request.user.company

        # Check if object already exists. Every instace has "pk" attribute
        # but only those which do not exist have pk=None (NULL in DB).
        # If so, continue this method. If not, create new record.
        # GUARD: Update of existing record (e.g. UpdateView)
        if form.instance.pk is not None:
            return super().form_valid(form)

        # Check for direct authorized relationship similar as above
        # in get_queryset() method.
        # GUARD (whole if and elif): Creation of new record (e.g. CreateView)
        if hasattr(form.instance, "company"):
            form.instance.comapany = user_company
        
        # Check for indirect authorized relationship similar as above
        # in get_queryset() method.
        elif hasattr(form.instance, "vendor"):
            vendor_pk = self.kwargs.get("pk")
            if vendor_pk:
                vendor_obj = get_object_or_404(Vendor, pk=vendor_pk, company=user_company)
                form.instance.vendor = vendor_obj
        
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        user_company = self.request.user.company

        # Filter vendors and load only those which are within
        # user's company workspace e.g. for dropdown options.
        if "vendor" in form.fields:
            form.fields["vendor"].queryset = Vendor.objects.filter(company=user_company)
        
        # Filter contracts and load only those which are within
        # selected contract selected vendor
        if "contract" in form.fields:
            filtered_data = form.fields["contract"].queryset.filter(vendor__company=user_company)
            form.fields["contract"] = filtered_data

        return form
    
