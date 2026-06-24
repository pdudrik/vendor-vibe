from django import forms
from .models import Vendor, Address, Contact


class CreateVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = [
            "name",
            "service_category",
            "status"
        ]

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = [
            "name",
            "service_category",
            "status"
        ]


class CreateVendorAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "street",
            "street_opt",
            "state_provinence",
            "postal_code",
            "country",
            "address_type"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["address_type"].initial = "BI"
        self.fields["country"].initial = "SK"


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "street",
            "street_opt",
            "state_provinence",
            "postal_code",
            "country",
            "address_type"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["address_type"].initial = "BI"
        self.fields["country"].initial = "SK"


class CreateVendorContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "number",
            "email"
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "number",
            "email"
        ]