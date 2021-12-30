# Modulo que responde as mensagens.

# TODO ainda não sei se vou criar um chatbot ou deixar o mais simples usando IF|CASE.


from pushbullet import PushBullet

def enviar_push(pb: PushBullet, mensagem: str) -> None:
    pb.push_note('Resposta', mensagem, device=pb.get_device('Xiaomi MI 9'))



