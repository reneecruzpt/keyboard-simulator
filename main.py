# main.py - Ponto de entrada do Simulador de Digitação

import sys
from PyQt5.QtWidgets import QApplication
from keyboard_simulator_pyqt5 import TypingTestApp

def main():
    app = QApplication(sys.argv)
    window = TypingTestApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
