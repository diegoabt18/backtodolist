from django.db import models

# Create your models here.
class Todolist(models.Model):
    Id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500)