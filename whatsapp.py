import pyautogui
import time

def enviar_mensagem_whatsapp(mensagem, quantidade):
    # Aguarda 5 segundos para você posicionar a janela do WhatsApp Web
    print("Posicione a janela do WhatsApp Web e o campo de mensagem...")
    time.sleep(5)
    
    for _ in range(quantidade):
        # Escreve a mensagem no campo de texto do WhatsApp
        pyautogui.write(mensagem)
        
        # Pressiona a tecla "Enter" para enviar
        pyautogui.press('enter')
        
        # Aguarda {x} segundos antes de enviar a próxima mensagem (para evitar sobrecarga)
        time.sleep(1)

# Exemplo de uso
mensagem = "TESTANDO"
quantidade = 5  # Quantidade de mensagens a enviar

enviar_mensagem_whatsapp(mensagem, quantidade)
