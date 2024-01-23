from django.db import models
from django.contrib.auth.models import AbstractUser
from .address import Address

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone_no = models.CharField(max_length=13)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False
        
    def isExists(self):
        if User.objects.filter(email=self.email):
            return True
        return False