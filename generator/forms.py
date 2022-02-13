from django import forms
from django.db import models
from .models import Scheme, SchemeColumn


class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = ['scheme_name', 'min_age', 'max_age', 'rows', 'quantity_of_sentences']


class SchemeColumnForm(forms.ModelForm):
    class Meta:
        model = SchemeColumn
        fields = ['column_type', 'name', 'order']
