import os
os.system("cls")

#ENTRADA

print("===========FRUTAS===============")
quantidade1 = float(input("digite a quantidade de morangos:"))
quantidade2 = float(input("digite a quantidade de maçãs:"))

#PROCESSAMENTO

if quantidade1 <= 5:
    preco_morango = quantidade1 * 2.50
    print("preço do morango:", preco_morango)
    
else:
   preco_morango =  quantidade1 * 2.20
   print("preço do morango:", preco_morango)

if quantidade2 <= 5:
    preco_maca = quantidade2 * 1.80
    print("preço da maçã:", preco_maca)
else:
   preco_maca = quantidade2 * 1.50
print("preço da maçã:", preco_maca)

total = preco_morango + preco_maca
quantidade_total = quantidade1 + quantidade2


if quantidade_total > 10 or total > 15:
   desconto = total * 0.10
   total = total - desconto
   print("voce recebeu 10% de desconto!")

print("Valor dos morangos:", preco_morango)
print("Valor das maçãs:", preco_maca)
print("Valor a pagar:", total)
    
