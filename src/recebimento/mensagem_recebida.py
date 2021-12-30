# Modulo com os dados de recebimento das mensagens.

from typing import Callable, Dict, List
from pushbullet import PushBullet


def recebimento_mensagem(pb: PushBullet) -> List[Dict]:
    """Pega todas as mensagens trocadas no pushbullet.

    Args:
        pb (PushBullet): Objeto inicializador do PushBullet.

    Returns:
        List[Dict]: Lista com todos os dados das mensagens.
    """
    mensagens = pb.get_pushes()
    return mensagens


def filter_mensagem(mensagens: List[Dict]) -> List[Dict]:
    """Remove todas as mensagens que foram enviadas como resposta do PC.

    Args:
        mensagens (List[Dict]): Lista com os dados das mensagens.

    Returns:
        List[Dict]: Lista com filtrada dos dados das mensagens.
    """
    return [mensagem for mensagem in mensagens if not mensagem.get('title')]


def ordenar_mensagem(mensagens: List[Dict]) -> List[Dict]:
    """Ordena as mensagens por data de envio.

    Args:
        mensagens (List[Dict]): Lista com os dados das mensagens.

    Returns:
        List[Dict]: Lista das mensagens ordenado por data de envio.
    """
    ordenado = sorted(mensagens, key=lambda code: float(code['created']))
    return ordenado


def pipeline(*funcs: Callable):
    """Faz um pipeline chamando as funções e passando os dados.
    """
    def inner(argumento):
        estado = argumento
        for func in funcs:
            estado = func(estado)
        return estado
    return inner


pipe = pipeline(recebimento_mensagem, filter_mensagem, ordenar_mensagem)
