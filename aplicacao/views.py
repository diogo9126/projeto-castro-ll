from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PessoaFisica, PessoaJuridica, Produto
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# -------------------- mixin customizado --------------------- #
class CustomGroupRequiredMixin():
    group_required = None
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not ( 
            self.request.user.is_superuser):                               
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)   


# ----------------- Views Produtos ----------------- #
class ProdutoCreateView(CustomGroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u'administradores'
    login_url = 'login'
    model = Produto
    fields = ['nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('listagem-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tituloP'] = "Cadastro de Produto"
        context['iconetitulo'] = '<i class="" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Produto"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Cadastrar'

        return context


# -------------------- PORTAL --------------------- #
class ProdutoListagemListView(CustomGroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'aplicacao/list/list-produto.html'    

    
class ProdutoDeleteView(CustomGroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"administradores"
    model = Produto
    template_name = 'aplicacao/delete.html'
    success_url = reverse_lazy('listagem-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-exclamation" aria-hidden="true"></i>'
        context['titulo'] = "Excluir Produto"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = 'excluir'

        return context


class ProdutoUpdateView(CustomGroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"administradores"
    model = Produto
    fields = ['nome', 'descricao', 'marca', 'preco', 'estoque', 'imagem', 'categoria']
    template_name = 'aplicacao/form.html'
    success_url = reverse_lazy('listagem-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Atualizar Produto"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Atualizar'

        return context


class ProdutoListView(ListView):
    model = Produto
    template_name = 'aplicacao/produto_list.html'


class ProdutoDetailView(DetailView):
    model = Produto
    

#-----------------   Views Pessoa Fisica ------------------------#

class PessoaFisicaCreate(CreateView):
    model = PessoaFisica
    fields= ['nome','sobre','cpf','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Física"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] ='Cadastrar'

        return context


class PessoaFisicaUpdate(LoginRequiredMixin,GroupRequiredMixin,UpdateView):
     group_required = u"administradores"
     model = PessoaFisica
     fields= ['nome','cpf','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
     template_name = 'aplicacao/formcliente.html'
     success_url = reverse_lazy('home')

     def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-group" aria-hidden="true"></i>'
        context['titulo'] = "Atualizar Cliente Pessoa Física"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'Atualizar'

        return context

class PessoaFisicaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = u"administradores"
    model = PessoaFisica
    template_name = 'aplicacao/delete.html'
    success_url = reverse_lazy('indexadmin')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Pessoa Fisica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['icon2'] = '<i class = "fa fa-reply" aria-hidden = "true" > </i >'
        context['botao'] = 'Excluir'

        return context


class PessoaFisicaListagemListView(LoginRequiredMixin,ListView):
    model = PessoaFisica
    template_name = 'aplicacao/list/list-cliente.html'


#---------------------- Views Pessoa Juridica ---------------------------#

class PessoaJuridicaCreate(CreateView):
    model = PessoaJuridica
    fields= ['nome','razao_social','cnpj','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fa fa-industry" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Juridica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'cadastrar'

        return context


class PessoaJuridicaUpdate(LoginRequiredMixin, GroupRequiredMixin,UpdateView):
    group_required = u"administradores"
    model = PessoaJuridica
    fields = ['nome','razao_social','cnpj','tipo','telefone','email','rua','numero','complemento','bairro','cidade','estado']
    template_name = 'aplicacao/formcliente.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['iconetitulo'] = '<i class="fas fa-building" aria-hidden="true"></i>'
        context['titulo'] = "Cadastro de Cliente Pessoa Juridica"
        context['icon']= '<i class="fa fa-check" aria-hidden="true"></i>'
        context['cadastrar'] = 'atualizar'

        return context 

    
class PessoaJuridicaDelete(LoginRequiredMixin,GroupRequiredMixin,DeleteView):
    group_required = u"administradores"
    model = PessoaJuridica
    template_name = 'aplicacao/delete.html'
    success_url = reverse_lazy('indexadmin')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Pessoa Juridica"
        context['icon'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['icon2'] = '<i class = "fa fa-reply" aria-hidden = "true" > </i >'
        context['botao'] = 'Excluir'

        return context


class PessoaJuridicaListagemListView(LoginRequiredMixin,ListView):
    model = PessoaJuridica
    template_name = 'aplicacao/list/list-juridico.html'
