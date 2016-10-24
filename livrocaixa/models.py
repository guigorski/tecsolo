from django.db import models
from django.utils import timezone
from django import forms

class Amostra(models.Model):

    Cliente = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ('A', 'MACRO'),
        ('I', 'MICRO'),
        ('F', 'FISICA'),
    )
    Amostras = models.CharField(max_length=1, choices=GENDER_CHOICES, default='NAO SELECIONADO')
    Data = models.DateTimeField(default=timezone.now)




    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Cliente
