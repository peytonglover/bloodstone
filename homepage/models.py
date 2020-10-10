from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    BU = 'Basic User'
    SU = 'Survey User'
    displayname =  models.CharField(max_length=80)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
    user_type_options = [
        (BU, 'Basic User'),
        (SU, 'Survey User')
    ]
    user_type = models.CharField(max_length=80, choices=user_type_options, default=BU)
    
