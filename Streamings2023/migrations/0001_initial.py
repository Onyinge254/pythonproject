# Generated by Django 4.2.1 on 2023-06-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField()),
                ('account_manager', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('account_name', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('product_type', models.CharField(max_length=255)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('crate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_before_comm_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
