from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages

from util.Messages import Messages as m

# Create your views here.
def login(request):
    return render(request, "login.html")

def valida_usuario(request):
    usuario = request.POST.get('apelido')
    senha = request.POST.get('senha')
    user = authenticate(username=usuario, password=senha)
    if user is not None:       
        auth_login(request,user)
        kwargs = {'usuario':usuario}
        return redirect('atrio',**kwargs)
    else:
        messages.error(request,m.ERRO_LOGAR_USUARIO.value)
        return redirect('login')
    
def registra_usuario(request):
    novo_usuario = request.POST.get('apelido_para_salvar')
    nova_senha = request.POST.get('senha_para_salvar')
    if User.objects.filter(username=novo_usuario).exists():
        messages.error(request, m.ERRO_CADASTRA_USUARIO.value)
        return redirect('login')
    user = User.objects.create_user(novo_usuario, password= nova_senha)
    user.save()
    messages.success(request,m.SUCESSO_SALVAR_USUARIO)
    return redirect('login')
