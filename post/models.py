from django.db import models
from datetime import date
# Create your models here.

class Author(models.Model):
  nombre_A = models.CharField(max_length = 50)
  correo = models.CharField(max_length = 50)


class Post(models.Model):
  titulo = models.CharField(max_length = 200)
  cuerpo = models.TextField()
  fecha  = models.DateField(default = date.today)
  author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True, blank = True)





