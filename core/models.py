from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(verbose_name='Data do Evento')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Criado em')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        db_table = 'evento'

    def __str__(self):
        return self.nome

    def get_data_evento(self):
        return self.data.strftime('%d/%m/%Y %H:%M')
