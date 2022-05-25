# -*- encoding: utf-8 -*-
from django import forms
from django.forms import formset_factory


class SchemaForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))


class ColumnForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    order = forms.CharField(widget=forms.NumberInput(attrs={"class": "input"}))
    data_type = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))


ColumnsFormSet = formset_factory(ColumnForm, extra=1)
