from snake import Snake
from fruit import Fruta
import os

class Game:

    def __init__(self):
        self.cobra = Snake((5, 7))
        self.fruta = Fruta((2, 8))
        self.tabuleiro = (10, 10)
        

    def verificar_fruta(self):
        if self.cobra.corpo[0] == self.fruta.posicao:
            self.cobra.comer()
            self.gerar_fruta_valida()

    def gerar_fruta_valida(self):
        self.fruta.gerar()

        while self.fruta.posicao in self.cobra.corpo:
            self.fruta.gerar()        
            


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

    def limpar_tela(self):
        if os.name == "nt": # SE FOR WINDOWS, USAR CLS
            os.system("cls")
        else: # SE FOR OUTRO OS, EXECUTAR O COMANDO CLEAR
            os.system("clear")   
    
    def gerar_tabuleiro(self):
        self.limpar_tela()

        lg, alt = self.tabuleiro
        print(" ------ SNAKE GAME --------")
        print("")
        if self.cobra.pontuacao > 1: 
            print(f"Pontuação autal: {self.cobra.pontuacao} pontos")
        else:
            print(f"Pontuação autal: {self.cobra.pontuacao} ponto")  


        
        for y in range(alt):
            linha = ""
            for x in range(lg):
                posicao = (x, y)

                if (posicao) == self.fruta.posicao:
                    linha += "[🍎]"
                elif(posicao) == self.cobra.corpo[0]:
                    linha += "[😛]"    
                elif (posicao) in self.cobra.corpo:
                    linha += "[🟩]"     
                else:
                    linha += "[  ]"

            print(linha)
        print(" ------ Versão 1.1 --------")     

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
        opcao = input("Digite X para jogar!  ").upper()
        print("+----------------------+")
         

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

            if self.verificar_borda() == True:
                self.game_over()
                self.jogo_rodando = False
                break
            elif self.verificar_colisao_cobra() == True:
                self.game_over()
                self.jogo_rodando = False
                break
            else:
                self.verificar_fruta()


    def game_over(self):

        print("+----------------------+")
        print("|      GAME OVER       |")
        print("+----------------------+")
        print(f"Sua pontuação final: {self.cobra.pontuacao} ponto(s)")

        opcao = input("Digite 'S' para tentar novamente e 'Q' para finalizar: ").upper()

        while opcao != "S"  and opcao != "Q":
            print("Opção inválida!")
            opcao = input("Digite 'S' para tentar novamente e 'Q' para finalizar: ").upper()

        if opcao == "Q":
            print("Até mais!")
            
        elif opcao == "S":
            self.executar()
                              


            

           

