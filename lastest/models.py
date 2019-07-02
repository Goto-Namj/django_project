from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10)
    idid = models.CharField(max_length=16)
    passpass = models.CharField(max_length=20)