import threading

tabuleiro=[[str(x) for x in range(3)] for x in range(3) ]
ganhador=False

class thread_verificar_ganhador(threading.Thread):


    
    def verificarHorizontal(self,simbolo):
        global tabuleiro
        for i in range(len(tabuleiro)):
            if(tabuleiro[i][0]==simbolo and tabuleiro[i][1]==simbolo and tabuleiro[0][2]):
                print(f"Ganhador {simbolo}")
                return True
        return False
    def verificarVertical(self, simbolo):
        global tabuleiro
        for i in range(len(tabuleiro)):
            if(tabuleiro[0][i]==simbolo and tabuleiro[1][i]==simbolo and tabuleiro[2][i]):
                print(f"ganhador simbolo {simbolo}")
                return True
        return False
    def verificarDiagonais(self, simbolo):
        global tabuleiro
        if(tabuleiro[0][0]==simbolo and tabuleiro[1][1]==simbolo and tabuleiro[2][2]
        or tabuleiro[0][2]==simbolo and tabuleiro[1][1]==simbolo and tabuleiro[2][0]
           ):
            print(f"ganhador simbolo {simbolo}")
            return True
        return False
    


        
    def run(self):
        global ganhador
        if(self.verificarVertical(simbolo="o")):
            ganhador=True
        elif(self.verificarHorizontal(simbolo="o")):
            ganhador=True
        elif(self.verificarVertical(simbolo="x")):
            ganhador=True
        elif(self.verificarHorizontal(simbolo="x")):
            ganhador=True
        elif(self.verificarDiagonais(simbolo="x")):
            ganhador=True
        elif(self.verificarDiagonais(simbolo="o")):
            ganhador=True




count=0
for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro)):
        tabuleiro[i][j]=count
        count+=1
def imprimirTabuleiro():
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            print(tabuleiro[i][j], end=" ")
        print("\n")

imprimirTabuleiro()


simbolo = input("Escolha seu simbolo O / X")
posicao = int(input("Escolha a posicao"))

t1=thread_verificar_ganhador()
t1.start()

while not ganhador:
    
    if(posicao==0):
        tabuleiro[0][0]=simbolo
    elif(posicao==1):
        tabuleiro[0][1]=simbolo
    elif(posicao==2):
        tabuleiro[0][2]=simbolo
    elif(posicao==3):
        tabuleiro[1][0]=simbolo
    elif(posicao==4):
        tabuleiro[1][1]=simbolo
    elif(posicao==5):
        tabuleiro[1][2]=simbolo
    elif(posicao==6):
        tabuleiro[2][0]=simbolo
    elif(posicao==7):
        tabuleiro[2][1]=simbolo
    elif(posicao==8):
        tabuleiro[2][2]=simbolo
    else:
        print("Posicao do tabuleiro nao econtrada")
    imprimirTabuleiro()
    simbolo = input("Escolha seu simbolo O / X")
    posicao = int(input("Escolha a posicao"))
  
