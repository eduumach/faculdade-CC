# Sabe-se que para iluminar de maneira correta os cômodos de uma casa, 
# para cada m2 deve-se usar 18 W de potência. 
# Escreva um algoritmo que leia as dimensões de um cômodo retangular (em metros), 
# calcule e mostre a sua área (em m2) e a potência de iluminação
# que deverá ser utilizada. 

largura = float(input("Digite a largura do comodo: "))
comprimento = float(input("Digite o comprimento do comodo: "))

metrosQuadrados = largura * comprimento

potenciaIluminacao = metrosQuadrados * 18

print("O seu comodo de", metrosQuadrados, "m2, vai precisa de", 
potenciaIluminacao, "W para iluminar seu comodo.")