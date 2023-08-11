def enviar_email(destinatario: str, assunto: str = "Sem assunto", corpo: str = ""):
    ''' Função para envio de um email '''
    print(f'''Destinatario: {destinatario}
Assunto: {assunto}
Corpo: {corpo}''')

destinatario = input("Digite o destinatario do e-mail: ")

enviar_email(destinatario)