from django.shortcuts import render,redirect,get_object_or_404

from .models import NumeroSecreto,Chute

def index(request,id_ns):     
    context = {"id_ns": id_ns}
    return render(request, "jogo/index.html", context)


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
        return render(request, "jogo/index.html", context)
    else:
        kwargs = {'id_ns':id_ns}
        return redirect('index',**kwargs)
