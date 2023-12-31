# Generated by Django 3.0.14 on 2023-07-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda_direta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='aceitar_termos',
            field=models.CharField(default='Sim', max_length=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cep',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cidade',
            field=models.CharField(default='Cidade Desconhecida', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cvv',
            field=models.CharField(default='000', max_length=3),
        ),
        migrations.AddField(
            model_name='usuario',
            name='data_validade',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(default='Endereço Desconhecido', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(default='Estado Deconhecido', max_length=50),
        ),
        migrations.AddField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outros', 'Outros')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nome_titular',
            field=models.CharField(default='Titular Desconhecido', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='receber_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='receber_sms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_cartao',
            field=models.CharField(choices=[('visa', 'Visa'), ('mastercard', 'Mastercard'), ('amex', 'American Express'), ('elo', 'Elo')], default='visa', max_length=20),
        ),
    ]
