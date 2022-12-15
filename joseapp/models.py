from django.db import models

# Create your models here.
class Alunos(models.Model):
 nome = models.CharField(max_length=100)
 endereco = models.CharField(max_length=100)
 email = models.CharField(max_length=100)
 telefone = models.CharField(max_length=50)
 cep = models.CharField (max_length=50)
 def __str__(self):
  return self.nome