#1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
#caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
#In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
#caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
#preluat automat de la tastatura.


name = input("Care este numele tau?\n")
sir = input("Introduceti un sir de caractere sau un sir de numere:\n")

result = any(char.isdigit() for char in sir)
if result == False:
    print(f"Sirul de caractere a fost gasit de {name}!")
else:
    print("Sirul introdus este un sir de numere")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
# numar este par sau impar si afisati un raspuns in acest sens.

print("Introduceti numarul dorit:\n")
int_numar = int(input())
if int_numar % 2 == 0:
    print("Numarul introdus este par!")
else:
    print("Numarul introdus este impar!")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
# la 4 (fara rest)

print("Introduceti anul dorit:")
an = int(input())
if an % 4 == 0:
   print("Anul este bisect!")
else:
   print("Anul nu este bisect!")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
# afisati numarul pozitiv.

print("Introduceti numarul dorit:")
numar = int(input())

if numar > 0:
    if numar < 10:
        print("Numar pozitiv mai mic decat 10")
elif  numar == 0:
    print("Numarul este zero")
else:
    print(abs(numar))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
# de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
# acest sir de caractere:
# “”” 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi “””
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”

print("Alegeti o optiune de mai jos:\n 1 – Afisare lista de cumparaturi\n 2 – Adaugare element\n 3 – Stergere element\n 4 – Sterere lista de cumparaturi\n 5 - Cautare in lista de cumparaturi")
nr_meniu = int(input())

if nr_meniu == 1:
    print("Afisare lista de cumparaturi")
elif nr_meniu == 2:
    print("Adaugare element")
elif nr_meniu == 3:
    print("Stergere element")
elif nr_meniu == 4:
    print("Sterere lista de cumparaturi")
elif nr_meniu == 5:
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")