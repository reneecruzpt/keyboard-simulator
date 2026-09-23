import time
import sys

def type_writer(text, delay=0.1):
    """
    Simula uma máquina de escrever, exibindo texto caracter por caracter.
    
    :param text: O texto a ser exibido.
    :param delay: O tempo de atraso entre cada caractere (em segundos).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Para quebrar a linha ao final do texto

# Exemplo de uso
if __name__ == "__main__":
    mensagem = (
        "Bem-vindo ao Reino de Velmoria...\n"
        "Prepare-se para uma jornada épica cheia de aventuras e desafios.\n"
        "Sua coragem será testada. Boa sorte, bravo herói!\n"
    )
    type_writer(mensagem, delay=0.05)
