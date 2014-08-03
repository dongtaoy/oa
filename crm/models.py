from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True)
    fax = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('crm.CustomerType', blank=True, null=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField('hr.Group', blank=True, null=True)


class CustomerType(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True)