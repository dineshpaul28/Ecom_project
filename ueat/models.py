from django.db import models

from djmoney.models.fields import MoneyField
from django.template.defaultfilters import slugify

# Create your models here.


class Product(models.Model):
    prod_name = models.CharField(max_length=50, null=True)
    prod_category = models.CharField(max_length=100, null=True)
    prod_subcategory = models.CharField(max_length=100, null=True)
    prod_desc = models.CharField(max_length=200)
    prod_price = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    prod_image = models.ImageField(upload_to='images', default="")
    slug = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.prod_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.prod_subcategory)
        return super().save(*args, **kwargs)


class Complained(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    phone = models.CharField(max_length=12, null=True)
    complaint = models.TextField(max_length=500)

    def __str__(self):
        return self.name + " " + self.city