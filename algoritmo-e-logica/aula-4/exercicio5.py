# O custo ao consumidor de um carro novo é a soma do custo de fábrica com 
# a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). 
# Supondo que a porcentagem do distribuidor seja de 28% e os impostos de 45%, 
# escreva um programa que leia o custo de fábrica de um carro e escreva o custo ao 
# consumidor.

custoFabrica = float(input("Digite o custo de fabrica: "))

distribuidor = custoFabrica * (28/100)
impostos = custoFabrica * (45/100)
consumidor = custoFabrica + distribuidor + impostos

print("\n------")
print("O custo do distribuidor eh:", distribuidor)
print("O custo dos impostos eh:", impostos)
print("-------")
print("O valor para o consumidor eh:", consumidor)