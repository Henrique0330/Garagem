from django.db import models

from core.models import Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField( blank=True, null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE, related_name='veiculos')
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, related_name='veiculos')
    acessorios = models.ManyToManyField(Acessorio, blank=True, related_name='veiculos')

    def __str__(self):
        return f'{self.id} - {self.modelo} - {self.cor} - {self.ano}'