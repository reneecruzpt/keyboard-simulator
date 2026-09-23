import sys
import time
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, QTimer


class TypingTestApp(QWidget):
    def __init__(self):
        super().__init__()

        # Lista de textos para digitação
        self.text_list = ["Hello World!", "Python is amazing.", "Keep practicing to improve.", "Code smarter, not harder."]
        self.reference_text = random.choice(self.text_list)  # Escolhe um texto aleatório
        self.typed_text = ""
        self.start_time = None
        self.end_time = None
        self.timer = QTimer(self)
        self.counter = 5
        self.errors = 0

        # Configuração da interface
        self.setWindowTitle('Typing Test')
        self.setGeometry(600, 200, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Texto de contagem regressiva
        self.countdown_label = QLabel("O teste inicia em: 5")
        self.countdown_label.setAlignment(Qt.AlignCenter)
        self.countdown_label.setStyleSheet('color: blue; font-size: 18px;')
        layout.addWidget(self.countdown_label)

        # Texto de referência que será mostrado inicialmente
        self.label = QLabel(self.reference_text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('color: grey;font-size: 18px;')  # Cor inicial (desativado)
        layout.addWidget(self.label)

        # Campo para digitação do usuário
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Aguarde a contagem regressiva...")
        self.text_input.setEnabled(False)
        self.text_input.textChanged.connect(self.on_text_changed)
        self.text_input.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text_input)

        self.setLayout(layout)

        # Inicia o contador regressivo
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)

    def update_countdown(self):
        """Atualiza o contador regressivo."""
        if self.counter > 0:
            self.countdown_label.setText(f"O teste inicia em: {self.counter}")
            self.counter -= 1
        else:
            self.timer.stop()
            self.start_test()

    def start_test(self):
        """Inicia o teste de digitação."""
        self.start_time = time.time()  # Marca o tempo de início
        self.countdown_label.setText("")  # Remove o texto do contador regressivo
        self.text_input.setEnabled(True)
        self.text_input.setFocus()

    def on_text_changed(self):
        """Verifica se o texto digitado é correto e atualiza a cor dos caracteres."""
        typed = self.text_input.text()
        current_errors = 0  # Erros na digitação atual

        # Atualiza o texto colorido
        updated_text = ""
        for i, char in enumerate(self.reference_text):
            if i < len(typed):
                if typed[i] == char:
                    updated_text += f'<span style="color: brown;">{char}</span>'  # Caractere correto
                else:
                    updated_text += f'<span style="color: red;">{char}</span>'  # Caractere incorreto
                    current_errors += 1
            else:
                updated_text += f'<span style="color: grey;">{char}</span>'  # Caractere não digitado

        # Atualiza o contador de erros acumulados
        self.errors += current_errors

        # Exibe o texto atualizado com a cor correta
        self.label.setText(updated_text)

        # Se a digitação for concluída, calcula o WPM
        if typed == self.reference_text:
            self.end_time = time.time()  # Marca o tempo de término
            self.calculate_wpm()

    def calculate_wpm(self):
        """Calcula as palavras por minuto e exibe a mensagem de sucesso."""
        elapsed_time = self.end_time - self.start_time
        elapsed_minutes = elapsed_time / 60

        # Cálculo do WPM baseado em 5 caracteres por palavra
        total_characters = len(self.reference_text)
        wpm = (total_characters / 5) / elapsed_minutes
        wpm = round(wpm, 2)

        # Exibe os resultados em uma QMessageBox
        self.show_result_message(wpm, elapsed_time)

    def show_result_message(self, wpm, elapsed_time):
        """Exibe a mensagem de sucesso com os resultados."""
        msg = QMessageBox(self)
        msg.setWindowTitle("Parabéns!")
        msg.setText(
            f"Você completou o teste com sucesso!\n\n"
            f"Palavras por minuto (WPM): {wpm}\n"
            f"Tempo gasto: {round(elapsed_time, 2)} segundos\n"
            f"Erros cometidos: {self.errors}"
        )
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        # Reinicia o teste
        self.reset_test()

    def reset_test(self):
        """Reinicia o teste para um novo texto."""
        self.reference_text = random.choice(self.text_list)  # Escolhe um novo texto aleatório
        self.label.setText(self.reference_text)
        self.label.setStyleSheet('color: grey;font-size: 18px;')  # Restaura a cor inicial
        self.text_input.clear()
        self.text_input.setEnabled(False)
        self.counter = 5
        self.errors = 0
        self.countdown_label.setText("O teste inicia em: 5")
        self.timer.start(1000)  # Reinicia o contador regressivo


# Função para rodar o aplicativo
def main():
    app = QApplication(sys.argv)
    window = TypingTestApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
