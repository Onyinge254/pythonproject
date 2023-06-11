from django.shortcuts import render
from .models import AccountInvoice
from .resources import AccountInvoiceResource
from django.contrib import messages
from tablib import dataset
from django.Http import HttpResponse

  def simple_upload(request):
      if request.method == 'POST':
        AccountInvoice_resource = AccountInvoiceResource()
        dataset=dataset()
        New_AccountInvoice= request.files('myfiles')

