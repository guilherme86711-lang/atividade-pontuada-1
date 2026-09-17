import os
os.system("cls")

#ENTRADA

A = int(input("digite o numero de A:"))
B = int(input("digite o numero de B:"))
C = int(input("digite o numero de C:"))

#PROCESSO

if A + B > C:
    print(f"O valor de: {A+B} é maior que {C}")
else:
    print(f"O valor de {A+B} é menor que {C}")
