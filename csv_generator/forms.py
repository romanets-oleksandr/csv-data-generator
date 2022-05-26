# -*- encoding: utf-8 -*-
from django import forms
from django.forms import modelformset_factory

from .models import Schema, Column
from . import data_type


class SchemaModelForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ('name', )
        labels = {
            'name': 'Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Name'
                }
            )
        }


ColumnFormset = modelformset_factory(
    Column,
    fields=('order', 'name', 'data_type',),
    extra=1,

    widgets={
        'order': forms.NumberInput(
            attrs={
                'class': 'input'
            }
        ),
        'name': forms.TextInput(
            attrs={
                'class': 'input',
            }
        ),
        'data_type': forms.Select(
            choices=data_type.get_choices()
        ),
    }
)
