print("Pense em um numero de 1 a 4...")
c = input("O numero é maior que 2? S ou N: ")

if c == 'S':
    c = input("O numero é maior que 3? S ou N: ")
    if c == 'S':
        print(4)
    else:
        print(3)
else:
    c = input("O numero é maior que 1? S ou N: ")
    if c == 'S':
        print(2)
    else:
        print(1)
