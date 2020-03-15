from django.db import models


class Lar(models.Model):
    porte_desejado = (
        ("P", "Pequeno"),
        ("M", "Médio"),
        ("G", "Grande"),
        ("I", "Indiferente")
    )


    pet_especial = (
        ("S", "Sim"),
        ("N", "Não")
    )

    nome = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True)
    porte_desejado = models.CharField(max_length=1, choices=porte_desejado, null=False, blank=False)
    pet_especial = models.CharField(max_length=1, choices=pet_especial, null=False, blank=False)
    criado_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Lar"
        verbose_name_plural = "Lares"
        ordering = ['nome']


    def __str__(self):
        return self.nome