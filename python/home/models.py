from django.db import models

class User(models.Model):
  userName = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  name = models.CharField(max_length=50)

class Card(models.Model):
  userid = models.IntegerField(default=0)
  stk = models.BigIntegerField(default=0)
  sd = models.IntegerField(default=0)
  bank = models.CharField(max_length=50)
