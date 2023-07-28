import re


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from util.Messages import Messages as m

# Create your views here.
def login(request):
    storage = messages.get_messages(request)
    for item in storage:
        pass
    return render(request, "login.html")

def valida_usuario(request):
    usuario = request.POST.get('apelido')
    senha = request.POST.get('senha')
    user = authenticate(username=usuario, password=senha)
    if user is not None:       
        auth_login(request,user)
        kwargs = {'usuario':usuario}
        messages.success(request,m.SUCESSO_LOGAR_USUARIO.value)
        return redirect('atrio_1',**kwargs)
    else:
        messages.error(request,m.ERRO_LOGAR_USUARIO.value)
        return redirect('login')

def registra_usuario(request):
    if request.method == 'GET':
        return redirect('login')  
    novo_usuario = request.POST.get('apelido')
    nova_senha = request.POST.get('senha')
    c = verifica_usuario_no_padrao(novo_usuario, nova_senha)
    if c: 
        try:
            user = User.objects.create_user(novo_usuario, password= nova_senha)
            user.save()
            messages.success(request,m.SUCESSO_CADASTRAR_USUARIO.value)
        except:
            messages.error(request,m.ERRO_CADASTRA_USUARIO.value)
    else:
        messages.error(request,m.ERRO_CADASTRA_USUARIO.value)
    return redirect('login')

def verifica_usuario_no_padrao(apelido, senha):
    if apelido == "" or senha == "":
        return False
    condicao_apelido = re.search("^([a-z0-9]){4,}$", apelido)
    condicao_senha = re.search("^(.){6,}$", senha)
    if condicao_apelido and condicao_senha:
        return True
    else:
        return False

@login_required
def fazer_logout(request):
    logout(request)
    return redirect('login')
