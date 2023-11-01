from django.db import models

class User(models.Model): # tạo bảng user có (username,password,name)
  userName = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  name = models.CharField(max_length=50)

class Card(models.Model): # tương tự
  userid = models.IntegerField(default=0)
  stk = models.BigIntegerField(default=0)
  sd = models.IntegerField(default=0)
  bank = models.CharField(max_length=50)
