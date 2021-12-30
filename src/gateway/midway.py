from typing import Dict, List, Literal, Optional

MODE = Literal['r', 'w',]

def _ler_code(mode: MODE, code: Optional[str] = None) -> str:
    _code = None
    if mode == 'w':
        with open('code.txt', mode) as f:
            _code = f.write(code)
    else:
        with open('code.txt', mode) as f:
            _code = f.read()
    return _code


def gravar_code(code:str) -> float:
    _ler_code('w', code=code)
    return code

def pega_code(mensagens: List[Dict]):
    codes = []
    for mensagem in mensagens:
        code = mensagem.get('created')
        if code:
            codes.append(code)
    return codes


def verifica_code(codes: List[Dict]) -> str:
    _code = _ler_code('r')
    for code in codes:
        if str(code) == str(_code):
            return True
    return False

        
