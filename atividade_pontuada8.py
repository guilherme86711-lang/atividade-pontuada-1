import os
os.system("cls")

#ENTRADA

cor = (input("digite uma cor: "))

#PROCESSAMENTO

match cor:
    case "verde":
        print("o valor do disco está 10,00.")
    case "azul":
        print("o valor do disco está 20,00.")
    case "amarelo":
        print("o valor do disco está 30,00.")
    case "vermelho":
        print("o valor do disco está 40,00.")
    
    case _:
        print("não possui no estoque.")
        