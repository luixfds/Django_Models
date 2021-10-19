from django.contrib import admin
from indexx.models import User, Produto


#   ADICIONANDO LIST_DISPLAY PARA COLOCAR VALORES E SEUS CABEÇALHOS
#   ADICIONANDO LIST_FILTER PARA COLOCAR CAIXA DE FILTRO
class UserView(admin.ModelAdmin):
    list_display = ('name', 'data_criacao')
    list_filter = ('name', 'data_criacao', )

class ProdutoView(admin.ModelAdmin):
    list_display = ('name','valor', 'quantidade')
    list_filter = ('name',)

#   DECLARANDO A TABELA NO ADMIN
admin.site.register(User, UserView)
admin.site.register(Produto, ProdutoView)