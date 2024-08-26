# Patinho vs Gatinho - Space Edition 🦆🚀🐱

**Versão:** 1.0  
**Desenvolvido por:** Ana Beatriz da Cunha

## 📝 Descrição

**Patinho vs Gatinho - Space Edition** é um jogo inspirado no famoso Angry Birds, mas ambientado no espaço! O jogador deve usar um canhão para lançar um patinho em direção a gatinhos estrategicamente posicionados, desviando de obstáculos gravitacionais, como a Lua, que aplica forças de repulsão no pato. O objetivo é acertar todos os gatinhos no menor número de tentativas possível.

Este jogo combina física realista, álgebra linear, resistência do ar e forças gravitacionais para criar uma experiência desafiadora e divertida.


## 🎮 Como Jogar

1. **Iniciar o Jogo:**  
   Ao iniciar o jogo, uma tela inicial será exibida. Clique em qualquer lugar para começar a jogar.

2. **Lançar o Patinho:**  
   Use o **mouse** para mirar e definir a direção e força do lançamento do patinho. Clique para disparar.

3. **Objetivo:**  
   Acerte os gatinhos com o patinho. Desvie da repulsão gravitacional da Lua para ter sucesso!

4. **Colisão:**  
   Quando o patinho colide com um gatinho, ele será derrubado. Acerte todos para ganhar o jogo!

5. **Resistência do Ar e Gravidade:**  
   A trajetória do patinho é afetada por resistência do ar e gravidade, criando uma simulação realista do movimento no espaço.


## 📚 Instruções de Instalação

### Pré-requisitos:

- **Python 3.11**  
  O jogo foi desenvolvido e testado usando o Python 3.11. Certifique-se de que essa versão esteja instalada no seu sistema.

  Para baixar e instalar o Python 3.11, acesse o site oficial através deste link: [Download Python 3.11](https://www.python.org/downloads/release/python-3110/)

### Instalando o Jogo

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/aninhaabc/Versao-angry-birds.git
   cd Versao-angry-birds

2. **Instalar o jogo com 'pip'**
    ```bash
    pip install git+https://github.com/aninhaabc/Versao-angry-birds.git

3. **Executar o jogo**
    ```bash
    ana_patinho_vs_gatinho

## 📽️ Vídeo Explicativo
Confira o vídeo explicativo sobre a matemática e a física por trás do jogo e veja o gameplay:

Link para o Vídeo no YouTube

## 💻 Estrutura do Código
A estrutura do código está dividida em módulos para facilitar o desenvolvimento e manutenção:

- jogo/: Contém os arquivos principais do jogo.

        - tela_inicial.py: Código responsável pela tela de abertura.

        - tela_final.py: Código responsável pela tela final de vitória.

        - tela_jogo.py: Lógica principal do jogo, contendo a física do lançamento, detecção de colisões, e aplicação das forças.

        - imagens: Imagens principais do jogo

        - fonte: Contém a fonte do jogo

