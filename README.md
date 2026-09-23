# Simulador de Digitação & Teste de Velocidade em Python (PyQt5)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green?logo=qt)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Aplicação desktop desenvolvida em **Python com PyQt5** para avaliação e treino de velocidade e precisão de digitação. O sistema calcula métricas em tempo real como **Palavras Por Minuto (WPM)** e **Precisão percentual**, além de incluir modos CLI e utilitários de máquina de escrever.

---

## ⚡ Funcionalidades

- **Interface Gráfica Desktop (PyQt5):**
  - Temporizador em tempo real com contagem decrescente.
  - Frases e desafios de texto aleatórios para teste.
  - Cálculo instantâneo de **WPM** (*Words Per Minute*) e taxa de acertos.
  - Caixa de diálogo com relatório detalhado de desempenho ao concluir.
- **Modo Terminal / CLI:**
  - Script interativo de consola (`keyboard_simulator_2.py`) para medição rápida de digitação no terminal.
  - Efeito visual de *Typewriter* animado com temporização de caracteres (`keyboard_simulator.py`).
- **Módulo de Algoritmos Complementares:**
  - Desafios clássicos de lógica na pasta `algoritmos/` (Verificação de Palíndromos, FizzBuzz e Sequência de Fibonacci).

---

## 📁 Estrutura do Repositório

```text
├── main.py                     # Ponto de entrada oficial da aplicação gráfica
├── keyboard_simulator_pyqt5.py # Implementação da classe da janela PyQt5
├── keyboard_simulator_2.py     # Versão de teste de WPM no terminal (CLI)
├── keyboard_simulator.py       # Efeito animado de máquina de escrever
├── algoritmos/                 # Desafios complementares de código
│   ├── fibonacci.py
│   ├── fizzbuzz.py
│   └── palindrome.py
└── requirements.txt            # Dependências da aplicação
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10 ou superior.

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/reneecruzpt/keyboard-simulator.git
   cd keyboard-simulator
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação gráfica:
   ```bash
   python main.py
   ```

*(Opcional) Para executar o teste direto no terminal:*
```bash
python keyboard_simulator_2.py
```

---

## 📄 Licença
Distribuído sob a licença MIT.
