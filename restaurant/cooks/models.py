from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        related_name="cook_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="cook_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    def get_absolute_url(self):
        return reverse("cooks:cook_detail", kwargs={"pk": self.pk})

