from enum import Enum
from django.contrib.messages import constants as messages


class Messages(Enum):
    # Sucesso 2x
    SUCESSO_CADASTRAR_USUARIO = 'sucess: 20'
    # Erro 4x
    ERRO_CADASTRA_USUARIO = 'erro: 40'
    ERRO_LOGAR_USUARIO = 'erro: 41'