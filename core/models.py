from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import os
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
import django
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(
        max_length=70, null=True, blank=True, help_text=' enter your first name')
    last_name = models.CharField(
        max_length=70, null=True, blank=True, help_text='enter your last name')
    username = models.CharField(
        max_length=70, unique=True, help_text=' username')
    password = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Salary(models.Model):
    employee = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    overtime = models.PositiveSmallIntegerField(null=True, blank=True)
    base_salary = models.FloatField(help_text='gross salary')
    bonuses = models.FloatField(editable=False, help_text='additional amount alongside gross salary'
                                )
    deductions = models.FloatField(help_text='all deductions from gross salary'
                                   )
    net_salary = models.FloatField(
        editable=False)

    def save(self, *args, **kwargs):
        self.net_salary = self.base_salary + self.bonuses - self.deductions
        super(Salary, self).save(*args, **kwargs)

    def __str__(self):
        return f'Employee name: {self.employee}, net salary: {self.net_salary}'

# after writing , or modifying models we make migrations and then migrate
# python manage.py makemigrations
# python manage.py migrate
