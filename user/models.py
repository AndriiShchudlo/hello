from django.db import models

# Create your models here.


class BaseUser(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    
    password = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    mobile_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username