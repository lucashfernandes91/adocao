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
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE,  related_name='ong')
    descricao = models.TextField(max_length=500)
    porte_desejado = models.CharField(max_length=1, choices=porte, null=False, blank=False)
    pet_especial = models.CharField(max_length=1, choices=pet_especial, null=False, blank=False)
    foto = models.FileField(upload_to='media/')
    #    criado_em = models.

    class Meta:
        verbose_name = "pet"
        verbose_name_plural = "pets"
        ordering = ['nome']

    def __str__(self):
        return self.nome

"""
class PetFoto(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='images')
    imagem = CloudinaryField('Imagem', blank=True, null=True)
    des = models.CharField('Descrição', max_length=200, blank=True, default='')

    def __str__(self):
        return self.pet.name

    class Meta:
        verbose_name = 'imagem pet'
        verbose_name = 'imagens do pet'"""