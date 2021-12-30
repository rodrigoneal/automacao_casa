from typing import Callable, Dict, List
from pushbullet import PushBullet

def recebimento_mensagem(pb: PushBullet) -> List[Dict]:
    mensagens = pb.get_pushes()
    return mensagens


def filter_mensagem(mensagens: List[Dict]) -> List[Dict]:
        return [mensagem for mensagem in mensagens if not mensagem.get('title')]


def ordenar_mensagem(mensagens: List[Dict]) -> List[Dict]:
    ordenado = sorted(mensagens, key=lambda code: float(code['created']))
    return ordenado

def pipeline(*funcs: Callable):
    def inner(argumento):
        estado = argumento
        for func in funcs:
            estado = func(estado)
        return estado
    return inner

pipe = pipeline(recebimento_mensagem, filter_mensagem, ordenar_mensagem)