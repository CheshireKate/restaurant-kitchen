from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()
    email = models.EmailField(unique=True)

    def get_absolute_url(self):
        return reverse("cooks:cook_detail", kwargs={"pk": self.pk})

