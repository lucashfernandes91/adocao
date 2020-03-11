from django.db import models

class adocao_temporaria(models.Model):
    nome = models.CharField(max_length=40)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    porte_desejado = models.CharField(max_length=2)
    idade = models.CharField(max_length=2)


    class Meta:
        verbose_name = "adoção temporária"
        verbose_name_plural = "adoções temporárias"


    def __str__(self):
        return self.nome