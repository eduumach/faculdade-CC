# Escreva um programa que calcule o valor do desconto de uma mercadoria paga a 
# vista e o valor total a ser pago. O programa deve ler o valor da mercadoria e 
# a porcentagem do desconto. Depois o programa deve calcular e imprimir na tela 
# o valor do desconto e o novo valor da mercadoria com o desconto.

valor = float(input("Escreva o valor da mercadoria: "))
porcentagem = float(input("Escreva o valor da porcentagem(sem o %):"))

valorDesconto = valor * (porcentagem/100)
totalPagar = valor - valorDesconto

print("-------")
print("Valor do produto:", valor, "reais.")
print("Porcentagem:", porcentagem, "porcento.")
print("Valor do desconto:", valorDesconto, "reais.")
print("Total a pagar:",totalPagar, "reais.")