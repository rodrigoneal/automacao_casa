from random import randint

import pytest

from src.recebimento.mensagem_recebida import (recebimento_mensagem, filter_mensagem,
                                      ordenar_mensagem, pipeline)
from config import pb


@pytest.fixture(scope='module')
def retorna_mensagens():
    return recebimento_mensagem(pb)


def test_se_recebimento_de_mensagem_esta_filtrando_mensagem(retorna_mensagens):
    mensagens = filter_mensagem(retorna_mensagens)
    esperado = 'title'
    assert not any(mensagem.get(esperado) for mensagem in mensagens)


def test_se_esta_ordenando_por_codigo_de_recebimento(retorna_mensagens):
    mensagem = ordenar_mensagem(retorna_mensagens)
    esperado_1 = mensagem[0]['created']
    esperado_2 = mensagem[-1]['created']
    assert esperado_1 <= esperado_2  # O igual é caso o tamanho da mensagem seja 1

def test_se_pipeline_chama_todas_as_funcoes():
    pipe = pipeline(recebimento_mensagem, filter_mensagem, ordenar_mensagem)
    mensagem = pipe(pb)
    esperado_1 = mensagem[0]['created']
    esperado_2 = mensagem[-1]['created']
    assert esperado_1 <= esperado_2  # O igual é caso o tamanho da mensagem seja 1
