# Cu ajutorul celor invatate in ultima saptamana la curs se va realiza un calculator, astfel:
# - calculatorul detine cifre de la 0 la 9,
# - semnele matematice cu ajutorul carora se vor putea realiza operatii matematice sunt urmatoarele: + (adunare), - (scadere), / (impartire), * (inmultire)
# - pe langa cifrele amintite anterior si semnele matematice se va putea sterge cu ajutorul litere C
# - toate operatiile presupun interactiunea cu utilizatorul (functii de tip input)

print("!!!!!CALCULATOR!!!!!")
print("Operatii permise: + (adunare), - (scadere), / (impartire), * (inmultire)")
while True:
    try:
        print("\n Introduceti valorile dorite cu spatiu intre ele:")
        a, oper, b = input().split()
        a = int(a)
        b = int(b)
        break
    except ValueError:
        print("Ati introdus date invalide. Mai incercati ...")

if oper == '+':
    print(a + b)
elif oper == '-':
    print(a - b)
elif oper == '*':
    print(a * b)
elif oper == '/':
    print(a / b)
