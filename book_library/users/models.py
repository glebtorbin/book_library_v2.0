from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fio = models.CharField('ФИО',max_length=200)
    phone_number = PhoneNumberField(unique = True, null = True, blank = False)

    def __str__(self):
        return self.username
