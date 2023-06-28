from django.db import models
from django.utils.translation import gettext_lazy as _


class Player(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    birth_date = models.DateField(null=False)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE, null=False)
