from django.contrib import admin
from indexx.models import Bot, Habilidade


#   ADICIONANDO LIST_DISPLAY PARA COLOCAR VALORES E SEUS CABEÇALHOS
#   ADICIONANDO LIST_FILTER PARA COLOCAR CAIXA DE FILTRO
class BotView(admin.ModelAdmin):
    list_display = ('apelido', 'data_criacao', 'status')
    list_filter = ('status',)


class HabilidadeView(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'quantidade')
    list_filter = ('status', )


#   DECLARANDO A TABELA NO ADMIN
admin.site.register(Bot, BotView)
admin.site.register(Habilidade, HabilidadeView)

#   USUARIO ADMIN
#   master masterpass master@master.com
