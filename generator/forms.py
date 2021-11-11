from django import forms
from django.db import models
from .models import Scheme


class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = ['scheme_name',
                  'choice1', 'choice2', 'choice3', 'choice4', 'choice5',
                  'choice6', 'choice7', 'choice8', 'choice9', 'choice10',
                  'name1', 'name2', 'name3', 'name4', 'name5',
                  'name6', 'name7', 'name8', 'name9', 'name10',
                  'order1', 'order2', 'order3', 'order4', 'order5',
                  'order6', 'order7', 'order8', 'order9', 'order10',
                  'min_age', 'max_age', 'rows', 'quantity_of_sentences'
                  ]
