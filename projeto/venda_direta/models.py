# venda_direta/models.py

from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, default='')
    data_nascimento = models.DateField()
    GENERO_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outros', 'Outros'),
    ]
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, null=True)
    endereco = models.CharField(max_length=100, default='Endereço Desconhecido')  # Adicione o valor padrão aqui
    cidade = models.CharField(max_length=100, default='Cidade Desconhecida')
    estado = models.CharField(max_length=50, default='Estado Deconhecido')
    cep = models.CharField(max_length=9, null=True)
    TIPO_CARTAO_CHOICES = [
        ('visa', 'Visa'),
        ('mastercard', 'Mastercard'),
        ('amex', 'American Express'),
        ('elo', 'Elo'),
    ]
    tipo_cartao = models.CharField(max_length=20, choices=TIPO_CARTAO_CHOICES, default='visa')
    nome_titular = models.CharField(max_length=100, null=True, blank=True)
    nome_titular = models.CharField(max_length=100, default='Titular Desconhecido')
    data_validade = models.CharField(max_length=5, null=True)  # Defina o campo como nulo
    cvv = models.CharField(max_length=3, default='000')
    receber_emails = models.BooleanField(default=False)
    receber_sms = models.BooleanField(default=False)
    aceitar_termos = models.CharField(max_length=200, default='Sim')

    def __str__(self):
        return self.nome
