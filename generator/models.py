from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Scheme(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scheme_name = models.CharField(max_length=255, unique=True)

    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=100)
    quantity_of_sentences = models.IntegerField(default=1)

    rows = models.IntegerField(default=1)
    task_progress = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='', blank=True)

    def __str__(self):
        return self.scheme_name


class SchemeColumn(models.Model):
    CHOICES = (
    (1, 'Name'),
    (2, 'Job'),
    (3, 'Email'),
    (4, 'Domain'),
    (5, 'Phone number'),
    (6, 'Company'),
    (7, 'Text'),
    (8, 'Age'),
    (9, 'Address'),
    (10, 'Date')
    )

    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    column_type = models.PositiveSmallIntegerField(choices=CHOICES, default=1)

    name = models.CharField(max_length=255, default="None")

    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = ('scheme', 'order')

    def __str__(self):
        return self.name
