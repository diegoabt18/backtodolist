from django.db import models

# Create your models here.
class Todolist(models.Model):
    tl_id = models.AutoField(primary_key=True)
    tl_titulo = models.CharField(max_length=500)
    tl_description =models.CharField(max_length=500)
    tl_date =models.DateField()
    tl_task=models.CharField(max_length=500)
    tl_state=models.BooleanField()

