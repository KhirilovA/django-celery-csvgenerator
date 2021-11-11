from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

CHOICES = (
    ('1', 'Choose'),
    ('2', 'Name'),
    ('3', 'Job'),
    ('4', 'Email'),
    ('5', 'Domain'),
    ('6', 'Phone number'),
    ('7', 'Company'),
    ('8', 'Text'),
    ('9', 'Age'),
    ('10', 'Address'),
    ('11', 'Date')
    )


class Scheme(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scheme_name = models.CharField(max_length=255, unique=True)

    choice1 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice2 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice3 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice4 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice5 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice6 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice7 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice8 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice9 = models.CharField(max_length=9, choices=CHOICES, default="1")
    choice10 = models.CharField(max_length=9, choices=CHOICES, default="1")

    name1 = models.CharField(max_length=255, default="None")
    name2 = models.CharField(max_length=255, default="None")
    name3 = models.CharField(max_length=255, default="None")
    name4 = models.CharField(max_length=255, default="None")
    name5 = models.CharField(max_length=255, default="None")
    name6 = models.CharField(max_length=255, default="None")
    name7 = models.CharField(max_length=255, default="None")
    name8 = models.CharField(max_length=255, default="None")
    name9 = models.CharField(max_length=255, default="None")
    name10 = models.CharField(max_length=255, default="None")

    order1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order7 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order8 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order9 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order10 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=100)
    quantity_of_sentences = models.IntegerField(default=1)

    rows = models.IntegerField(default=1)
    task_progress = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='', blank=True)








