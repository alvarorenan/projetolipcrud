from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
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

    def get_data_input_evento(self):
        return self.data.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data < datetime.now():
            return True
        else:
            return False

    def get_telefone_whitout_mask(self):
        return self.telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

    def get_dia(self):
        return self.data.strftime('%d/%m/%Y')
    def get_hora(self):
        return self.data.strftime('%H:%M')
