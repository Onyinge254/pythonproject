from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AccountInvoice

class AccountInvoiceAdmin(ImportExportModelAdmin):
    list_display = ('account_no', 'account_manager', 'branch', 'account_name', 'client', 'product', 'product_type',
                    'amount_paid', 'crate', 'amount_before_comm_tax', 'commission', 'vat', 'total', 'month', 'year')

admin.site.register(AccountInvoice, AccountInvoiceAdmin)
