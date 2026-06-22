from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
    
    
    

class Employee(AbstractUser):
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        related_name="employees",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username