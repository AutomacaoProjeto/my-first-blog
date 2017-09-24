from django.db import models

# Create your models here.

# class Pessoa(models.Model):
# 	rg = models.IntegerField(primary_key=True)
# 	cpf = models.IntegerField()
# 	nome = models.CharField(max_length=70)
# 	email = models.EmailField(max_length=70) 
# 	"""Existe um campo tipo email??"""
# 	senha = models.CharField(max_length=30)
# 	"""Existe um campo tipo senha??"""

# class Cliente(models.Model):
	
# 	rg_pessoa = models.ForeingKey(Pessoa)

# class Funcionario(models.Model):
# 	rg_pessoa = models.ForeingKey(Pessoa)

# class Gerente(models.Model):
# 	rg_pessoa = models.ForeingKey(Pessoa)

# class Linha(models.Model):
# 	rg_funcionario = models.ForeingKey(Funcionario)
# 	cod = models.IntegerField(primary_key=True)

# class Trajeto(models.Model):
# 	cod_linha = models.ForeingKey(Linha)
# 	"""COLOCAR COMO CHAVE PRIMARIA"""
# 	cidades = models.CharField(max_length=30)
# 	"""COLOCAR COMO CHAVE PRIMARIA"""

# 	"""select tc.telefone from cliente c, TelefoneCliente tc where c.cpf = tc.cpfClient"""

# class Passagem(models.Model):
# 	rg_cliente = models.ForeingKey(Cliente) 
# 	"""COLOCAR COMO CHAVE PRIMARIA"""
# 	cod_assento = models.ForeingKey(Assento)
# 	"""COLOCAR COMO CHAVE PRIMARIA"""
# 	cod_it = models.ForeingKey(Intinerario)
# 	"""COLOCAR COMO CHAVE PRIMARIA"""
# 	h_compra = models.DateTimeField()
# 	h_viagem = models.DateTimeField()
# 	valor = models.DecimalField(max_length=5, decimal_places=2)