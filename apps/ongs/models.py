from django.db import models


class Ong(models.Model):
    nome = models.CharField(max_length=40)
    responsavel = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    cidade = models.CharField(max_length=50)
    criado_em = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = "ong"
        verbose_name_plural = "ongs"
        ordering = ['nome']


    def __str__(self):
        return self.nome