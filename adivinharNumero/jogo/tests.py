from django.contrib.auth.models import User
from django.test import TestCase, Client

class TestJogo(TestCase):
    def setUp(self):
        self.password = '123456'

        self.username1 = 'usuario1'
        self.user1 = User.objects.create_user(
            username=self.username1,
            password=self.password
        )
        self.username2 = 'usuario2'
        self.user2 = User.objects.create_user(
            username=self.username2,
            password=self.password
        )

    def test_acessa_atrio_usuario1_sem_estar_logado_falha(self):
        client = Client()
        response = client.get(f'/usuario/{self.username1}/atrio/')
        self.assertEqual(response.status_code, 403)

    def test_acessa_atrio_usuario1_logado_com_usuario2_falha(self):
        client = Client()
        client.force_login(self.user2)
        response = client.get(f'/usuario/{self.username1}/atrio/')
        self.assertEqual(response.status_code, 403)

    def test_acessa_atrio_usuario1_logado_com_usuario1_sucesso(self):
        client = Client()
        client.force_login(self.user1)
        response = client.get(f'/usuario/{self.username1}/atrio/')
        self.assertEqual(response.status_code, 200) 

