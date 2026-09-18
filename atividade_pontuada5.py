import os
os.system("cls")

#ENTRADA

a = int(input("digite um número: "))
b = int(input("digite um número: "))

print("==escolha uma operação==")
operacao = (input("escolha uma operação:"))

#PROCESSO

match operacao:
    case "soma":
        soma = print("resultado", a+b)
    case "subtração":
        subtracao = print("resultado", a-b)
    case "multiplicação":
        multiplicacao = print("resultado", a*b)
    case "divisão":
        divisao = print("resultado", a/b)
    case "nenhum":
        print("necessário informar uma operação.")

#SAIDA
print("///FIM ALGORITMO///")