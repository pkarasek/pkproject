from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Company(models.Model):
    company_name = models.CharField(max_length = 50, null = False, blank = False)
    company_contact = models.CharField(max_length = 50, null = True)
    
    
    def __str__(self):
        return self.company_name
    
