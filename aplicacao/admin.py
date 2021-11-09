from django.contrib import admin

from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria')
    fields = ('nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria')