from django.db import models


class AccountInvoice(models.Model):
    account_no = models.CharField(max_length=100,null=True)
    account_manager = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    crate = models.DecimalField(max_digits=10, decimal_places=2)
    amount_before_comm_tax = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"Account No: {self.account_no}, Account Manager: {self.account_manager}, Branch: {self.branch}, " \
               f"Account Name: {self.account_name}, Client: {self.client}, Product: {self.product}, " \
               f"Product Type: {self.product_type}, Amount Paid: {self.amount_paid}, Crate: {self.crate}, " \
               f"Amount Before Comm&Tax: {self.amount_before_comm_tax}, Commission: {self.commission}, " \
               f"VAT(16%): {self.vat}, Total: {self.total}, Month: {self.month}, Year: {self.year}"
