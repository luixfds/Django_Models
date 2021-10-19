from django.db import models


#   TABELA DO BANCO CRIADA ATRAVES DOS MODELS DJANGO
class User(models.Model):
    #   CAMPOS DA TABELA E SEUS TIPOS
    name = models.CharField(max_length=30, verbose_name='Nome de Usuario')
    # apelido = models.TextField(blank=True, null=True)
    apelido = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20)
    # senha = models.TextField()
    senha = models.CharField(max_length=10)
    nascimento = models.DateField()
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data do Registro')

    #   DEFININDO NOME DA TABELA NO BANCO
    class Meta:
        db_table = 'usuario'
    #   MOSTRANDO OS REGISTROS COM O NOME DOS TAIS
    def __str__(self):
        return self.name


class Produto(models.Model):
    name = models.CharField(max_length=20)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'produtin'

    def __str__(self):
        return self.name