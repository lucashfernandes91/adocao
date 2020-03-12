from django.db import models
from apps.ongs.models import Ong

class Pet(models.Model):

    porte = (
        ("P", "Pequeno"),
        ("M", "Médio"),
        ("G", "Grande")
    )

    pet_especial = (
        ("S", "Sim"),
        ("N", "Não")
    )


    nome = models.CharField(max_length=40)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    ong = models.OneToOneField(Ong, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=500)
    porte_desejado = models.CharField(max_length=1, choices=porte, null=False, blank=False)
    pet_especial = models.CharField(max_length=1, choices=pet_especial, null=False, blank=False)


    class Meta:
        verbose_name = "pet"
        verbose_name_plural = "pets"


    def __str__(self):
        return self.nome
