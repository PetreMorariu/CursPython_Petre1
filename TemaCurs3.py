#Declara o lista

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
list_asscend = my_list.copy()
list_asscend.sort()
print("Lista sortata crescator este" , list_asscend)
print("Lista initiala este" ,my_list)


#afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
list_descend = my_list.copy()
list_descend.sort(reverse=True)
print("\nLista sortata descrescatore este" , list_descend)
print("Lista initiala este" ,my_list)


#afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
print("\nLista de numere pare este", list_asscend[1::2])

#afișează o listă ce conține numerele impare din lista ordonată (folosind slice
print("\nLista de numere impare este", list_asscend[::2])

#afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).
print("\nLista de numere multiplu de 3 este", list_asscend[2::3])



