from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, UserViewSet, login_view

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', views.pagina_inicial, name='inicio'),
    path('home/', views.pagina_home, name='home'),
    path('login/', views.pagina_login, name='login'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('produtos/', views.pagina_produtos, name='produtos'), 
    path('carrinho/', views.pagina_carrinho, name='carrinho'), 
    path('checkout/', views.pagina_checkout, name='checkout'), 
    path('colecao1/', views.pagina_colecao1, name='colecao1'),
    path('colecao2/', views.pagina_colecao2, name='colecao2'),
    path('colecao3/', views.pagina_colecao3, name='colecao3'),
    path('colecao4/', views.pagina_colecao4, name='colecao4'),
    path('colecoes/', views.pagina_colecoes, name='colecoes'),

    path('api/', include(router.urls)),
    path('api/login/', login_view),
]