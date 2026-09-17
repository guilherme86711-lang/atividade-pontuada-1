import os
os.system("cls")

#ENTRADA

nome = (input("digite seu nome:"))
sexo = (input("digite seu sexo F OU M:"))
estado_civil = (input("digite seu estado civil:"))

#PROCESSO

if sexo == "F" and estado_civil == "casada":
    tempo = int(input("digite em anos o tempo de casada:"))

print("nome: ", nome)
print("sexo", sexo)
print("Estado civil", estado_civil)

if sexo == "F" and estado_civil == "casada":
    print("tempo de casada:", tempo, "anos")



