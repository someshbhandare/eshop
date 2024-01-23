from django.db import models

class Address(models.Model):
    street_address = models.CharField(max_length=128, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)
    pin_code = models.CharField(max_length=6, null=False)

    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}, {self.state}, {self.country}, {self.pin_code}"