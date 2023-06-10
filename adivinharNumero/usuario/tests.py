from django.contrib.auth.models import User
from django.test import TestCase, Client

class TestUsuario(TestCase):
    def setUp(self):
        # Cria um usuário de teste
        self.username = 'usuario1'
        self.password = '123456'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    def test_login_acessoGet(self):
        client = Client()
        response = client.get('/usuario/login/')
        self.assertEqual(response.status_code, 200) 

    def test_login_usuario1_sucesso(self):
        client = Client()
        response = client.post('/usuario/login/check/', {'apelido': self.username, 'senha': self.password})        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/usuario/{self.username}/atrio/')
    
    def test_login_falsoUsuario_falha(self):
        client = Client()
        username = 'falsoUsuario'
        response = client.post('/usuario/check/', {'apelido': username, 'senha': self.password})                
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/usuario/login/')