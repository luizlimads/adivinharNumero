from django.contrib.auth.models import User
from django.test import TestCase, Client
from util.Messages import Messages as m
"""
    Classe para realização de testes automaticos no app usuarios
    Nome de testes seguindo a seguinda logica
    test_<Objeto de teste>_<Opcional>_<Tipo de ação>_<Retorno esperado>
    Para este app
    Objeto de teste:
        >login - acesso ou fluxo de login
        >loginCheck - acesso a rota check de login
        >register - acesso ou fluxo de register
        >registerCheck - acesso a rota check de register
    Opcional - contexto
    Tipo de ação:
        >acessa - acessa uma rota com o metodo GET 
        >loga - acessa rota de login com metodo POST
        >registra - acessa rota de register com metodo POST
    Retorno esperado:
        >sucesso
        >falha
        >redireciona
"""
class TestUsuarioViews(TestCase):
    def setUp(self):
        # Cria um usuário de teste
        self.username = 'usuario1'
        self.password = '123456'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    # Seccao verificar funcionalidade de logar
    def test_login_acessa_sucesso(self):
        client = Client()
        response = client.get('/usuario/login/')
        self.assertEqual(response.status_code, 200) 

    def test_loginCheck_acessa_redireciona(self):
        client = Client()
        response = client.get('/usuario/login/check/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/usuario/login/')

    def test_login_usuarioForaDePadrao_loga_falha(self):
        client = Client()
        test_data = [
            {'apelido': '', '': self.password}, # usuario e senha vazios
            {'apelido': 'jao', 'senha': self.password}, # usuario menor que 4 letras
            {'apelido': self.username, 'senha': 'ddd'}, # senha menor que 6 digitos
            {'apelido': 'Jaos', 'senha': self.password}, # usuario com letra maiuscula
            {'apelido': 'joão', 'senha': self.password}, # usuario com acento
            {'apelido': 'joao teste', 'senha': self.password}, # usuario com espaço em branco
        ]
        for data in test_data:
            response = client.post('/usuario/login/check/', data)
            messages = [m.message for m in response.wsgi_request._messages]
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/usuario/login/')
            self.assertIn(messages[0], m.ERRO_LOGAR_USUARIO.value)
   
    def test_login_usuario1_loga_sucesso(self):
        client = Client()
        response = client.post('/usuario/login/check/', {'apelido': self.username, 'senha': self.password})        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/usuario/{self.username}/atrio/')
    
    def test_login_usuarioErrado_loga_falha(self):
        client = Client()
        username = 'usuario_errado'
        response = client.post('/usuario/login/check/', {'apelido': username, 'senha': self.password})                
        messages = [m.message for m in response.wsgi_request._messages]
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/usuario/login/')
        self.assertEqual(len(messages),1)
        self.assertEqual(messages[0],m.ERRO_LOGAR_USUARIO.value)

    # Seccao verifica funcionalidade de registro
    def test_registerCheck_acessa_redireciona(self):
        client = Client()
        response = client.get('/usuario/register/check/')
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, '/usuario/login/')

    def test_register_usuarioNovoRegistra_registra_sucesso(self):
        client = Client()
        response = client.post('/usuario/register/check/', {'apelido': self.username+'teste', 'senha': self.password})
        messages = [m.message for m in response.wsgi_request._messages]
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/usuario/login/')
        self.assertEqual(len(messages),1)
        self.assertEqual(messages[0],m.SUCESSO_CADASTRAR_USUARIO.value)

    def test_register_usuarioForaDePadrao_registra_falha(self):
        client = Client()
        test_data = [
            {'apelido': '', '': self.password}, # usuario e senha vazios
            {'apelido': 'jao', 'senha': self.password}, # usuario menor que 4 letras
            {'apelido': self.username, 'senha': 'ddd'}, # senha menor que 6 digitos
            {'apelido': 'Jaos', 'senha': self.password}, # usuario menos com letra maiuscula
            {'apelido': 'joão', 'senha': self.password}, # usuario com acento
            {'apelido': 'joao teste', 'senha': self.password}, # usuario com espaço em braco
        ]
        for data in test_data:
            response = client.post('/usuario/register/check/', data)
            messages = [m.message for m in response.wsgi_request._messages]
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, f'/usuario/login/')
            self.assertIn(messages[0], m.ERRO_CADASTRA_USUARIO.value)
    
    def test_register_usuarioExistente_registra_falha(self):
        client = Client()
        response = client.post('/usuario/register/check/', {'apelido': self.username, 'senha': self.password})
        messages = [m.message for m in response.wsgi_request._messages]
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/usuario/login/')
        self.assertEqual(len(messages),1)
        self.assertEqual(messages[0],m.ERRO_CADASTRA_USUARIO.value)