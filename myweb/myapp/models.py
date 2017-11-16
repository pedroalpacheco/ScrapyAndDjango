from django.db import models

class Person(models.Model):
    data = models.TextField(blank=True, null=True)
    compra = models.TextField(blank=True, null=True)

