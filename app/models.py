from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    Role_Choices=(
        ('User','User'),
        ('Admin','Admin'),
        ('Moderator','Moderator'),
    )
    role=models.CharField(max_length=10, choices=Role_Choices)


