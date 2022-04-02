from django.db import models

# Create your models here.
class Todolist(models.Model):
    tl_id = models.AutoField(primary_key=True)
    tl_nombre = models.CharField(max_length=500)