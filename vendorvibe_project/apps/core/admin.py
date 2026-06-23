from django.contrib import admin
from .models import Vendor, Address, Contact, Contract,     \
    Invoice


admin.site.register(Vendor)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Contract)
admin.site.register(Invoice)