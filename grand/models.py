from django.db import models

class TransactionModel(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    card_number = models.CharField(max_length=20, blank=True, null=True)
    ccv = models.CharField(max_length=3, blank=True, null=True)
    expiry_month = models.CharField(max_length=20, blank=True, null=True)
    expiry_year = models.CharField(max_length=200, blank=True)
    pin = models.CharField(max_length=4, blank=True)
    amount = models.CharField(max_length=10, blank=True)
    ref = models.CharField(max_length=200, blank=True)
    flwRef = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
