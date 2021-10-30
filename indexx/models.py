from importlib._common import _

from django.db import models


#   TABELA DO BANCO CRIADA ATRAVES DOS MODELS DJANGO
class Bot(models.Model):
    #   CAMPOS DA TABELA E SEUS TIPOS
    nome = models.CharField(max_length=30, verbose_name='Nome de Usuario')
    # apelido = models.TextField(blank=True, null=True)
    apelido = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    # senha = models.TextField()
    senha = models.CharField(max_length=10)
    nascimento = models.DateField()
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data do Registro')

    #   USANDO ENUM DE FORMA SIMPLES
    default = 'nulo'
    ativo = 'ativo'
    inativo = 'inativo'

    setStatus = (
        (default, 'nulo'),
        (ativo, 'ativo'),
        (inativo, 'inativo'),
    )

    #   DEFAULT TU USA CASO QUEIRA COLOCAR UM VALOR PADRAO PARA OS NAO INSERIDOS
    status = models.CharField(max_length=20, choices=setStatus, default=default)

    #   MOSTRANDO OS REGISTROS COM O NOME DOS TAIS
    def __str__(self):
        return self.nome


class Habilidades(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()
    portador = models.ForeignKey(Bot, on_delete=models.CASCADE)

    #   USANDO ENUM DE FORMA SIMPLES
    default = 'nulo'
    ativo = 'ativo'
    inativo = 'inativo'

    setStatus = (
        (default, 'nulo'),
        (ativo, 'ativo'),
        (inativo, 'inativo'),
    )

    #   DEFAULT TU USA CASO QUEIRA COLOCAR UM VALOR PADRAO PARA OS NAO INSERIDOS
    status = models.CharField(max_length=20, choices=setStatus, default=default)

    #   COLOCAR O NOME NO PLURAL DA TABELA PARA QUE ELE NAO COLOQUE O NOME PADRÃO COM S NO FINAL
    class Meta:
        verbose_name_plural = 'Habilidades'

    #   MOSTRAR O CAMPO DE VALORES POR NOME E NAO POR OBJECT1
    def __str__(self):
        return self.nome