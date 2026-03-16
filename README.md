# 🦇 Bat Cave Escape

**Bat Cave Escape** é um jogo 2D desenvolvido em **Python** utilizando a biblioteca **Pygame**.
O jogador controla um morcego que precisa escapar de uma caverna cheia de estalactites, desviando dos obstáculos e tentando alcançar a maior pontuação possível.

Este projeto foi desenvolvido como prática de **lógica de programação**, **orientação a objetos** e **desenvolvimento de jogos com Python**.

---

# 🎮 Gameplay

![Gameplay](batCaveEscape/assets/video-demonstrativo.gif)

O objetivo do jogo é simples:

* Controlar o morcego
* Desviar dos obstáculos da caverna
* Sobreviver o máximo possível
* Aumentar sua pontuação

A dificuldade aumenta conforme o jogador progride, com os obstáculos ficando cada vez mais rápidos.

---

# 🕹️ Controles

| Tecla             | Ação               |
| ----------------- | ------------------ |
| **SPACE**         | Pular / Voar       |
| **R**             | Reiniciar o jogo   |
| **ESC**           | Voltar para o menu |
| **Fechar janela** | Encerrar o jogo    |

---

# ✨ Funcionalidades

* 🎮 Sistema de menu inicial
* 🦇 Controle do personagem (morcego)
* 🪨 Obstáculos gerados aleatoriamente
* 📈 Sistema de pontuação
* 🔊 Efeitos sonoros
* 🎵 Música de fundo
* 💀 Tela de Game Over
* ⚡ Aumento progressivo da dificuldade

---

# 🗂️ Estrutura do Projeto

```
BatCaveEscape
│
├── main.py
├── requirements.txt
│
├── config
│   ├── settings.py
│   └── states
│       ├── menu.py
│       └── game_over.py
│
├── entities
│   ├── player.py
│   └── obstacle.py
│
└── assets
    ├── imgs
    │   ├── cave_background.png
    │   ├── logo.png
    │   └── stalactite.png
    │
    └── sounds
        ├── jump.mp3
        ├── hit.wav
        ├── score.wav
        ├── game_over.wav
        └── music.mp3
```

---

# ⚙️ Tecnologias Utilizadas

* Python
* Pygame

Conceitos aplicados:

* Programação orientada a objetos
* Game loop
* Manipulação de eventos
* Colisão entre objetos
* Estrutura modular de projeto

---

# ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/bat-cave-escape.git
```

### 2️⃣ Entrar na pasta do projeto

```bash
cd bat-cave-escape
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar o jogo

```bash
python main.py
```

---

# 📦 Gerar Executável (.exe)

Para gerar um executável do jogo:

```bash
python -m PyInstaller --onefile --windowed --name BatCaveEscape main.py
```

Após gerar o executável, copie a pasta **assets** para dentro da pasta **dist**.

Estrutura final:

```
dist
│
├── BatCaveEscape.exe
└── assets
    ├── imgs
    └── sounds
```

---

# 📚 Objetivos do Projeto

Este projeto foi criado para praticar:

* Desenvolvimento de jogos com Python
* Estruturação de projetos em múltiplos módulos
* Manipulação de gráficos e sons
* Lógica de gameplay
* Criação de executáveis para distribuição

---

# 🚀 Possíveis Melhorias Futuras

* 🏆 Sistema de **High Score**
* 🎨 Animação do personagem
* 🌌 Fundo com **parallax**
* 🦇 Novos tipos de obstáculos
* 🎮 Sistema de níveis
* 💾 Salvamento de progresso

---

# 👨‍💻 Autor

Desenvolvido por **Jey Victor Malta Mateó dos Santos**

Estudante de **Análise e Desenvolvimento de Sistemas**
Focado em **desenvolvimento de software, lógica de programação e desenvolvimento de jogos com Python**.

---
