from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != "POST":
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('password')

    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, "Usuário ou senha inválidos!")
        return render(request, 'accounts/login.html')

    auth.login(request, user)
    messages.success(request, "Logado com sucesso!")
    return redirect('dashboard')

    # print(request.POST)

    messages.success(request, "Logado com sucesso!")
    return redirect('login')


def logout(request):
    # return render(request, 'accounts/logout.html')
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    if request.method != 'POST':
        messages.warning(request, 'Informe os campos!')
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    password = request.POST.get('password')
    password_confirm = request.POST.get('password_confirm')

    if(password != password_confirm):
        messages.error(request, "Senhas não conferem!")
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, "Email inválido!")
        return render(request, 'accounts/cadastro.html')

    if not nome or not sobrenome or not email or not usuario or not password:
        messages.error(request, 'Informe os campos!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'accounts/cadastro.html')

    user = User.objects.create_user(username=usuario, email=email, password=password, first_name=nome, last_name=sobrenome)
    messages.success(request, "Registrado com sucesso! Faça login com os dados informados")
    user.save()

    print(request.POST['usuario'])
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
