from snake import Snake
from fruit import Fruta

class Game:

    def __init__(self):
        self.cobra = Snake((5, 7))
        self.fruta = Fruta((2, 8))
        self.tabuleiro = (10, 10)

    def verificar_fruta(self):
        if self.cobra.corpo[0] == self.fruta.posicao:
            self.cobra.comer(self.fruta)
            

