import time

def calculate_wpm(start_time, end_time, typed_text, reference_text):
    """
    Calcula palavras por minuto (WPM).
    :param start_time: Tempo inicial do teste.
    :param end_time: Tempo final do teste.
    :param typed_text: Texto digitado pelo usuário.
    :param reference_text: Texto de referência que foi exibido.
    :return: WPM e precisão como uma tupla (wpm, accuracy).
    """
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60
    
    # Contar palavras digitadas
    word_count = len(typed_text.split())
    
    # Calcular WPM
    wpm = word_count / elapsed_minutes
    
    # Calcular precisão
    reference_words = reference_text.split()
    typed_words = typed_text.split()
    correct_words = sum(1 for tw, rw in zip(typed_words, reference_words) if tw == rw)
    accuracy = (correct_words / len(reference_words)) * 100 if reference_words else 0
    
    return round(wpm, 2), round(accuracy, 2)

def typing_test():
    """
    Realiza o teste de digitação.
    """
    reference_text = (
        "O Reino de Velmoria precisa de heróis valentes para enfrentar desafios. "
        "Este é o seu momento para brilhar."
    )
    print("\nTeste de Digitação:")
    print(reference_text)
    print("\nDigite o texto acima exatamente como aparece e pressione Enter quando terminar.\n")
    
    # Captura o tempo de início
    input("Pressione Enter para começar...")
    start_time = time.time()
    
    # Entrada do usuário
    typed_text = input("\nSua digitação: ")
    
    # Captura o tempo de término
    end_time = time.time()
    
    # Calcula WPM e precisão
    wpm, accuracy = calculate_wpm(start_time, end_time, typed_text, reference_text)
    
    # Exibe os resultados
    print("\nResultados:")
    print(f"Palavras por minuto (WPM): {wpm}")
    print(f"Precisão: {accuracy}%")
    print(f"Tempo gasto: {round(end_time - start_time, 2)} segundos")
    print("\nObrigado por participar!")

# Executa o teste
if __name__ == "__main__":
    typing_test()

