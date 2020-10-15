from django.db import models

class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
