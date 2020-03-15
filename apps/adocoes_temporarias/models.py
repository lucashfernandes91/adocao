from django.db import models


class Adocao_temporaria(models.Model):

    porte_desejado = (
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
    email = models.EmailField(max_length=50, unique=True)
    porte_desejado = models.CharField(max_length=1, choices=porte_desejado, null=False, blank=False)
    pet_especial = models.CharField(max_length=1, choices=pet_especial, null=False, blank=False)
    criado_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "adoção temporária"
        verbose_name_plural = "adoções temporárias"


    def __str__(self):
        return self.nome
