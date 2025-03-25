import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def enviar_email(smtp_server, smtp_port, remetente, senha, destinatario, assunto, mensagem, quantidade):
    try:
        # Conecta ao servidor SMTP
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()  # Conecta usando TLS (para segurança)
        
        # Faz o login na conta de e-mail
        servidor.login(remetente, senha)
        
        for _ in range(quantidade):
            # Cria o e-mail
            msg = MIMEMultipart()
            msg['From'] = remetente
            msg['To'] = destinatario
            msg['Subject'] = assunto
            
            # Adiciona a mensagem no corpo do e-mail
            msg.attach(MIMEText(mensagem, 'plain'))
            
            # Envia o e-mail
            servidor.sendmail(remetente, destinatario, msg.as_string())
            print(f'E-mail enviado para {destinatario}')
            
            # Aguardar 1 segundo antes de enviar o próximo e-mail
            time.sleep(1)
        
        # Fecha a conexão com o servidor
        servidor.quit()
        print('Todos os e-mails foram enviados com sucesso!')
    
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Informações do remetente
smtp_server = 'smtp.gmail.com'  # Para Gmail
smtp_port = 587  # Porta para envio com TLS
remetente = 'exemplo123@gmail.com'  # Substitua pelo seu e-mail
senha = ' '  # Substitua pela sua senha (recomendado usar senhas de app, não a senha principal)
destinatario = 'meuamigo123@gmail.com'  # Substitua pelo e-mail do destinatário
assunto = 'teste' #O assunto do email
mensagem = 'teste' #A mensagem do email
quantidade = 10  # Quantidade de e-mails a enviar

# Chama a função para enviar os e-mails
enviar_email(smtp_server, smtp_port, remetente, senha, destinatario, assunto, mensagem, quantidade)
