nota = float(input("Digite sua nota: "))

if (nota >= 9.0):
    print("Conceito A")
elif (nota < 9.0) and (nota > 8.0):
    print("Conceito B")
elif (nota < 8.0 )and (nota >= 7.0):
    print("Conceito C")
elif (nota < 7.0) and (nota >= 6.0):
    print("Conceito D")
else:
    print("Conceito F")
