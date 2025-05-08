from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    birth_year = models.DateField()

    def __str__(self):
        return self.full_name
