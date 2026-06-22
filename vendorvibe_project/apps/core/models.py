from django.db import models
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField


CATEGORIES = {
    "MA": "Marketing",
    "LE": "Legal",
    "FI": "Finance",
    "IT": "IT Support",
    "GO": "Goods"
}

VENDOR_STATUS = {
    "active": "Active",
    "inactive": "Inactive"
}

ADDRESS_TYPES = {
    "BI": "Billing",
    "SH": "Shipping",
    "HQ": "Headquarters"
}

INVOICE_STATUS_OPTIONS = {
    "DR": "Draft",
    "PE": "Pending",
    "PA": "Paid",
    "OV": "Overdue"
}


class Vendor(models.Model):

    name = models.CharField(
        max_length=50
    )
    service_category = models.CharField(
        max_length=2,
        choices=CATEGORIES
    )
    status = models.CharField(
        max_length=10,
        choices=VENDOR_STATUS
    )

    class Meta:
        verbose_name_plural = "Vendors"

    def __str__(self):
        return self.name


class Address(models.Model):
    vendor_id = models.ForeignKey(
        Vendor,
        on_delete=models.SET_NULL,
        null=True
    )
    street = models.CharField(
        max_length=60
    )
    street_opt = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    state_provinence = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    postal_code = models.CharField(
        max_length=10
    )
    country = CountryField()
    address_type = models.CharField(
        max_length=2,
        choices=ADDRESS_TYPES
    )

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        if self.vendor_id:
            return self.vendor.name
        return f"Vendor NULL to record id: {self.id}({self.street})"
    

class Contact(models.Model):
    vendor_id = models.ForeignKey(
        Vendor,
        on_delete=models.SET_NULL,
        null=True
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=30
    )
    middle_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    number = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    email = models.EmailField(
        max_length=50,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Contacts"

    def clean(self):
        super().clean()
        if not self.number and not self.email:
            raise ValidationError("Number or email must be filled!")

    def __str__(self):
        return self.name
    

class Contract(models.Model):
    vendor_id = models.ForeignKey(
        Vendor,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(
        max_length=30
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Contracts"

    def __str__(self):
        return self.name
    

class Invoice(models.Model):
    contcract_id = models.ForeignKey(
        Contract,
        on_delete=models.SET_NULL,
        null=True
    )
    invoice_id = models.CharField(
        max_length=30,
        unique=True,
    )
    ammount = MoneyField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        default_currency="EUR"
    )
    issue_date = models.DateField()
    issue_date = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=INVOICE_STATUS_OPTIONS
    )
    invoice_file = models.FileField(
        upload_to="invoices/",
        null=True,
        blank=True
    )


    class Meta:
        verbose_name_plural = "Invoices"

    def __str__(self):
        return self.name
    


    
