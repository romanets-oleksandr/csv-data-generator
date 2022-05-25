from django.db import models


class Schema(models.Model):
    name = models.CharField(max_length=200)
    modified = models.DateTimeField(auto_now_add=True)


class Column(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    data_type = models.CharField(max_length=50)
