from django.db import models

# Create your models here.


class Something(models.Model):
    message = models.CharField(max_length=200)


class SomethingElse(models.Model):
    something = models.ForeignKey(Something, on_delete=models.CASCADE, null=True)
