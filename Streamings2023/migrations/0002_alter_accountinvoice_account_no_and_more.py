# Generated by Django 4.2.1 on 2023-06-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Streamings2023', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinvoice',
            name='account_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='accountinvoice',
            name='month',
            field=models.CharField(max_length=20),
        ),
    ]
