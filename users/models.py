from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None

    nickname = models.CharField(max_length=15, unique=True, verbose_name="닉네임")

    def __str__(self):
        return self.nickname
