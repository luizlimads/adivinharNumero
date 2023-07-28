from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NumeroSecreto,Chute
from django.http import HttpResponseForbidden


def redireciona_atrio(request, usuario):
    kwargs = {'usuario':usuario}
    return redirect("atrio_1",**kwargs)

@login_required
def atrio_1(request,usuario):
    if request.user.username != usuario:
        return HttpResponseForbidden(f"Acesso restrito apenas para o usuário {usuario}.")
    return render(request, "atrio/estatisticas_gerais.html")

@login_required
def atrio_2(request,usuario):
    if request.user.username != usuario:
        return HttpResponseForbidden(f"Acesso restrito apenas para o usuário {usuario}.")
    return render(request, "atrio/serie_temporal.html")

def redireciona_jogo(request, usuario):
    kwargs = {'usuario':usuario}
    return redirect("jogo_1",**kwargs)

@login_required
def jogo_1(request,usuario):
    if request.user.username != usuario:
        return HttpResponseForbidden(f"Acesso restrito apenas para o usuário {usuario}.")
    return render(request, "jogo/um_jogador.html")

@login_required
def jogo(request,id_ns):     
    context = {"id_ns": id_ns}
    return render(request, "jogo.html", context)


def check(request,id_ns):
    numero_secreto = get_object_or_404(NumeroSecreto, pk=id_ns)
    valor_chute = int(request.POST.get('chute'))
    chute = Chute(
        id_segredo = numero_secreto,
        tentativa = valor_chute,
        )
    chute.save()
    if(numero_secreto.segredo == valor_chute):
        tentativas = Chute.objects.filter(id_segredo_id=id_ns).count()
        context = {'id_ns': id_ns,
                   'check':True,
                   'tentativas':tentativas}
        return render(request, "jogo.html", context)
    else:
        kwargs = {'id_ns':id_ns}
        return redirect('jogo',**kwargs)
