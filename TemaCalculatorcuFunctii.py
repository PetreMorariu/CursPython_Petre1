def adunare(a, b):
    return a + b


def scadere(a, b):
    return a - b


def inmultire(a, b):
    return a * b


def impartire(a, b):
    return a / b


if __name__ == '__main__':
    pass

print("!!!!!CALCULATOR!!!!! \n Operatii permise: + (adunare), - (scadere), / (impartire), * (inmultire)")
while True:
    try:
        print("Introduceti valorile dorite cu spatiu intre ele:")
        a, oper, b = input().split()
        a = int(a)
        b = int(b)
        break
    except ValueError:
        print("Valorile introduse nu sunt valide. Mai incercati ...")

if oper == '+':
    print(adunare(a, b))
elif oper == '-':
    print(scadere(a, b))
elif oper == '*':
    print(inmultire(a, b))
elif oper == '/':
    print(impartire(a, b))
else:
    print("Operatorul nu este valid!!")
    exit()
