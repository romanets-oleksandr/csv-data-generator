from django.db import models
from . import data_type


class Schema(models.Model):
    name = models.CharField(max_length=200)
    modified = models.DateTimeField(auto_now_add=True)


class Column(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    data_type = models.CharField(max_length=50, choices=data_type.get_choices())

    min_range = models.IntegerField(default=0)
    max_range = models.IntegerField(default=0)


class DataSet(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    csv_file = models.FileField(upload_to='csv')
