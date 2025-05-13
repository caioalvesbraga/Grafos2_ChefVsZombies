# Grafos2_ChefVsZombies
![Demonstração](assets/demo.gif)
**Número da Lista**: X<br>
**Conteúdo da Disciplina**: Grafos 2<br>
**Video da apresentação**: [Grafos2_ChefVsZombies
](https://youtu.be/zb7NTT11jgI)<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 211030694 | Caio Felipe Alves Braga |


## Sobre  
Este projeto é uma aplicação desenvolvida com **Pygame** para a disciplina de PA, como continuação da exploração de algoritmos de grafos.  
Desta vez, implementamos uma solução baseada no **Problema do Caixeiro Viajante (TSP)** para ajudar um chef desastrado a coletar ingredientes em um cenário caótico, repleto de zumbis dançarinos. O chef deve visitar todos os ingredientes seguindo o menor caminho possível, enquanto desvia dos zumbis.

## Screenshots
![image](https://github.com/user-attachments/assets/af8e7f7a-a324-473a-9621-9d74c87278f3)

![image](https://github.com/user-attachments/assets/20a22cee-0483-4cf4-ba6d-97747af46ebf)


## Instalação
**Linguagem**: Python  
**Framework**: Pygame  

### Pré-requisitos
- Python 3.x  
- Pygame  

### Comandos para instalação
1. Instale o Python 3.x.
2. Instale o Pygame utilizando o pip:

```bash
pip install pygame
```

## Uso
### Passo a passo
1. Execute o script principal do projeto:

```bash
python main.py
```

2. O jogo será iniciado com o chef no centro da tela. Os ingredientes aparecerão aleatoriamente no mapa, e os zumbis começarão a se mover em direção ao chef.

3. O algoritmo resolve o TSP para determinar a melhor ordem de coleta dos ingredientes. O caminho ideal é desenhado na tela.

4. Movimente o chef com as setas do teclado para coletar os ingredientes, enquanto evita ser pego pelos zumbis dançarinos.

5. Ao coletar todos os ingredientes, você vence. Se for alcançado por um zumbi, o jogo termina.

### Outros
Configurações adicionais: Você pode modificar parâmetros como número de ingredientes ou inimigos diretamente no código, ajustando as funções gerar_ingredientes ou inimigos.
