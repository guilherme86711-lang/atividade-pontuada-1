import os
os.system("cls")

#ENTRADA

print("Combustível	Quantidade Vendida	Desconto por Litro")
print(" Álcool	       Até 25 litros	      10%")
print("Álcool	       Acima de 25 litros	  20%")
print("Gasolina	      Até 25 litros	          15%")
print("Gasolina	     Acima de 25 litros	      30%")

litros = float(input("Digite a quantidade de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A - Álcool / G - Gasolina): ")

# PROCESSAMENTO

if combustivel == "A" or combustivel == "a":

    preco = litros * 3.79

    if litros <= 25:
        desconto = preco * 0.10
    else:
        desconto = preco * 0.20

elif combustivel == "G" or combustivel == "g":

    preco = litros * 6.59

    if litros <= 25:
        desconto = preco * 0.15
    else:
        desconto = preco * 0.30

else:
    print("Tipo de combustível inválido.")
    desconto = 0
    preco = 0

total = preco - desconto

# SAÍDA

print("Valor sem desconto:", preco)
print("Desconto:", desconto)
print("Valor a pagar:", total)

print("///FIM ALGORITMO///")