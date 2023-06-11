from import_export import resources
from .models import AccountInvoice

Class AccountInvoiceResource(Resources.modelresource):
    class meta:
        model = AccountInvoice
