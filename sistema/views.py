from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Produto
from .serializers import ProdutoSerializer, UserSerializer

# Páginas HTML
def pagina_inicial(request):
    return render(request, 'Inicial.html')

def pagina_home(request):
    return render(request, 'home.html')

def pagina_login(request):
    return render(request, 'login.html')

def pagina_cadastro(request):
    return render(request, 'cadastro.html')

def pagina_produtos(request):
    return render(request, 'produtos.html')

def pagina_carrinho(request):
    return render(request, 'carrinho.html')

def pagina_checkout(request):
    return render(request, 'checkout.html')

def pagina_colecao1(request):
    return render(request, 'coleção1.html')

def pagina_colecao2(request):
    return render(request, 'coleção2.html')

def pagina_colecao3(request):
    return render(request, 'coleção3.html')

def pagina_colecao4(request):
    return render(request, 'coleção4.html')

def pagina_colecoes(request):
    return render(request, 'coleções.html')

# API
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        return Response({'message': 'Login realizado com sucesso', 'user_id': user.id})
    else:
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)