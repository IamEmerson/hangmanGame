# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Função limpa a tela


def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Classe


class Hangman:
    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letra_escolhida = []
        self.letras_erradas = []

        # Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letra_escolhida:
            self.letra_escolhida.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

        # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)

        # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

        # Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letra_escolhida:
                rtn += '_'
            else:
                rtn += letra
        return rtn

        # Método para checar o status do game e imprimir o board na tela

    def print_game_status(self):
        print(board[len(self.letras_erradas)])

        # Palavra
        print('\nPalavra: ' + self.hide_word())

        # letra errada
        print('\nLetras erradas: ', ' '.join(self.letras_erradas))

        # letra correta
        print('\nLetras corretas: \n', ' '.join(self.letra_escolhida))


def rand_word():
    palavras = ['Banana', 'Morango', 'Maracuja', 'Laranja', 'Uva']
    palavra = random.choice(palavras)
    return palavra


def main():
    # Cria o objeto e seleciona uma palavra randomicamente
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        #  Status do game
        game.print_game_status()

        # Recebe input do terminal
        user_input = input('Digite uma letra: ')

        # Verifica se a letra digitada faz parte da palavra
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
