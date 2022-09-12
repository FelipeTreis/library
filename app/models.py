from django.db import models

from app.api.choices import STATE_CHOICES


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class PublishingCompany(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.ManyToManyField(Category)
    state = models.CharField(
        max_length=15, choices=STATE_CHOICES,
        null=False, blank=False
    )
    publishing_company = models.ForeignKey(
        PublishingCompany, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    is_available = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
