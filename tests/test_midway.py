from src.gateway.midway import gravar_code, verifica_code, pega_code
from src.recebimento.mensagem_recebida import pipe
from config import pb

def test_se_mensagem_esta_gravando_texto_com_o_code():
    code = gravar_code('123456789')
    esperado = '123456789'
    with open('code.txt','r') as f:
        assert f.read() == esperado

def test_se_verifica_code_encontra_ler_codigo_e_retorna_true():
    code = verifica_code(['123456789'])
    esperado = True
    assert code == esperado

def test_se_verifica_code_encontra_ler_codigo_e_retorna_false():
    code = verifica_code(['987654321'])
    esperado = False
    assert code == esperado

def test_se_pega_code_retorna_uma_lista_dos_codigos():
    lista_codigo = [{'created': code} for code in range(0, 50)]
    code = pega_code(lista_codigo)
    assert len(code) == 49

def test_integracao_das_funcoes_de_midway():
    pass
