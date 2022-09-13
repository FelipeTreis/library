from django.db import models

from app.api.choices import LANGUAGE_CHOICES, STATE_CHOICES


class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    biography = models.TextField(null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return self.full_name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class PublishingCompany(models.Model):
    class Meta:
        verbose_name_plural = 'Publishing Companies'

    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.ManyToManyField(Category)
    num_pages = models.IntegerField(default=1)
    state = models.CharField(
        max_length=8, choices=STATE_CHOICES,
        null=False, blank=False
    )
    language = models.CharField(
        max_length=10, choices=LANGUAGE_CHOICES,
        null=True, blank=False
    )
    author = models.ManyToManyField(Author)
    publishing_company = models.ForeignKey(
        PublishingCompany, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
