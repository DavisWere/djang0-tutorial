from django.db import models

# Create your models here.
from django.db import models


class Salary(models.Model):
    employee_name = models.CharField(max_length=100)
    base_salary = models.FloatField()
    bonuses = models.FloatField(
    )
    deductions = models.FloatField(
    )
    net_salary = models.FloatField(
        editable=False)

    def save(self, *args, **kwargs):
        self.net_salary = self.base_salary + self.bonuses - self.deductions
        super(Salary, self).save(*args, **kwargs)

    def __str__(self):
        return f'Employee name: {self.employee_name}, net salary: {self.net_salary}'

# after writing , or modifying models we make migrations and then migrate
# python manage.py makemigrations
# python manage.py migrate
