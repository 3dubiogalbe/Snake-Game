class Snake:

    def __init__(self, posicao):
        """"
        (__init__) >> Cria o objeto com um estado inicial, com os atributos de posição e pontuação
        para cada cobra individualmente (por isso o self)
        """
        self.corpo = [posicao] # ATRIBUTO
        self.pontuacao = 0 # ATRIBUTO
        self.crescer_no_prox_mov = False

    def mover(self, direcao):
        """"
        Criação do método (método = ação) de movimento da cobra.
        Move a cobra para a direção informada.

        Args:
            direcao (str): W, A, S ou D.
        """
        self.direcao = direcao
        x, y = self.corpo[0] # Aqui "abrimos" a tupla que tem a posição da cabeça

        if direcao == "W":
            y -= 1
            nova_cabeca = (x, y)
            self.corpo.insert(0, nova_cabeca)
        elif direcao == "A":
            x -= 1
            nova_cabeca = (x, y)
            self.corpo.insert(0, nova_cabeca)
        elif direcao == "S":
            y += 1
            nova_cabeca = (x, y)
            self.corpo.insert(0, nova_cabeca)
        elif direcao == "D":
            x += 1
            nova_cabeca = (x, y) 
            self.corpo.insert(0, nova_cabeca) 
            
        if self.crescer_no_prox_mov == True:
            self.crescer_no_prox_mov = False
        else:
            self.corpo.pop()
                      

    def comer(self):
        """
        Aumenta a pontuação da cobra e informa à fruta que ela foi consumida.

        Args:
            None.
        """
        self.pontuacao += 1
        self.crescer()
        
        

    def crescer(self):
        self.crescer_no_prox_mov = True
        


   