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

    def verificar_borda(self):
        x, y = self.cobra.corpo[0]
        lg, alt = self.tabuleiro

        if x >= lg or x < 0:
            return True
        elif y >= alt or y < 0:
            return True
        else:
            return False
        
    def verificar_colisao_cobra(self):
        cabeca = self.cobra.corpo[0]

        for partes in self.cobra.corpo[1:]:
            if cabeca == partes:
                return True
            
        return False 
    def gerar_tabuleiro(self):
        lg, alt = self.tabuleiro
        
        for y in range(alt):
            linha = ""
            for x in range(lg):
                posicao = (x, y)

                if (posicao) == self.fruta.posicao:
                    linha += "F"
                elif (posicao) in self.cobra.corpo:
                    linha += "C" 
                else:
                    linha += "."

            print(linha) 

    def mostrar_menu(self):
        print("+----------------------+")
        print("|      SNAKE GAME      |")
        print("+----------------------+")
        print("")
        print("+----------------------+")
        print("|    Por Eduardo Bio   |") 
        print("+----------------------+")

                
    def executar(self):
        self.mostrar_menu()
        print("+----------------------+")
        print("Digite X para jogar!   ")
        print("+----------------------+")

        opcao = input(">> ").upper()

        while opcao != "X":
            print("Tecla inválida, digite novamente: ")
            opcao = input(">> ").upper()
    
        self.jogo_rodando = True

        while self.jogo_rodando == True:
            self.gerar_tabuleiro()
            direcoes = ["W", "A", "S", "D", "Q"]    
            direcao = input("Digite uma direção: (W A S D) e Q para sair: ").upper()

            while direcao not in direcoes:
                print("Digite uma direção válida!")
                direcao = input("Digite uma direção: (W A S D) ").upper()

            if direcao == "Q":
                print("Até mais! ")
                self.jogo_rodando = False
                break
               
            self.cobra.mover(direcao)
            self.verificar_fruta()


            if self.verificar_borda() == True:
                self.game_over()
                self.jogo_rodando = False
                break
            elif self.verificar_colisao_cobra() == True:
                self.game_over()
                self.jogo_rodando = False
                break


    def game_over(self):

        print("+----------------------+")
        print("|      GAME OVER       |")
        print("+----------------------+")                


            

           

