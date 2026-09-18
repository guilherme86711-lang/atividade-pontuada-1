import os
os.system("cls")

#ENTRADA

nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota: "))

#PROCESSAMENTO
media = (nota1 + nota2)/ 2

if media >= 6:
    print("parabéns você foi aprovado.")
elif media >= 4.1 or media <=5.9:
    print("você está em recuperação")
else:
    print("você foi reprovado.")