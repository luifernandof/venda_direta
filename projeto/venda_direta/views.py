# venda_direta/views.py

from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def index(request):
    return render(request, 'venda_direta/index.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        telefone = request.POST['telefone']
        data_nascimento = request.POST['data-nascimento']
        genero = request.POST['genero']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        cep = request.POST['cep']
        tipo_cartao = request.POST['tipo-cartao']
        numero_cartao = request.POST['numero-cartao']
        nome_titular = request.POST['nome-titular']
        data_validade = request.POST['data-validade']
        cvv = request.POST['cvv']
        receber_emails = request.POST.get('receber-emails', False)
        receber_sms = request.POST.get('receber-sms', False)
        aceitar_termos = request.POST.get('aceitar-termos', False)

        usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            data_nascimento=data_nascimento,
            genero=genero,
            endereco=endereco,
            cidade=cidade,
            estado=estado,
            cep=cep,
            tipo_cartao=tipo_cartao,
            numero_cartao=numero_cartao,
            nome_titular=nome_titular,
            data_validade=data_validade,
            cvv=cvv,
            receber_emails=receber_emails,
            receber_sms=receber_sms,
            aceitar_termos=aceitar_termos
        )
        usuario.save()

        # Redirecionar para uma página de sucesso ou outra página desejada
        return redirect('pagina_sucesso')

    return render(request, 'venda_direta/cadastro.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para a página inicial após o cadastro
    else:
        form = UsuarioForm()
    return render(request, 'venda_direta/cadastro.html', {'form': form})

def extrato(request):
    return render(request, 'venda_direta/extrato.html')

def compras(request):
    return render(request, 'venda_direta/compras.html')

def rastreamento(request):
    return render(request, 'venda_direta/rastreamento.html')

def catalogo(request):
    return render(request, 'venda_direta/catalogo.html')

def comissao(request):
    return render(request, 'venda_direta/comissao.html')

def marketing(request):
    return render(request, 'venda_direta/marketing.html')

def dashboard(request):
    return render(request, 'venda_direta/dashboard.html')

def suporte(request):
    return render(request, 'venda_direta/suporte.html')

def atendimento(request):
    return render(request, 'venda_direta/atendimento.html')





    # Adicione outras visualizações aqui, conforme necessário
