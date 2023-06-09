from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    # user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    # user.save()
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
        return redirect('login')