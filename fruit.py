import random

class Fruta:
    def __init__(self, posicao):
        self.posicao = posicao

    def gerar(self): # PARAMETRO SÓ EXISTE QUANDO O USUÁRIO PRECISAR PASSAR ALGO! (ou seja, o usuário determina a posição da fruta? NAAAAO, por isso tiramos "posicao" dai.)
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        self.posicao = (x, y)
