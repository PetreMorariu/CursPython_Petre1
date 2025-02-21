def meniu():
    submeniu2 = '0'
    submeniu3 = '0'

    print("""
    1. Listare date 
    2. Sortare: se alege o opțiune din cele 8 de mai jos:
    3. Filtrare date
    4. Adauga un nou task/taskuri
    5. Editarea detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task
    6. Ștergerea unui task din lista inițială.
    """)

    meniu1 = input()
    if meniu1 == '1':
        pass
    elif meniu1 == '2':
        print("""
         Criteriile disponibile sunt:
           1. sortare ascendentă task
           2. sortare descendentă task
           3. sortare ascendentă data
           4. sortare descendentă data
           5. sortare ascendentă persoana responsabilă
           6. sortare descendentă persoană responsabilă
           7. sortare ascendentă categorie
           8. sortare descendentă categorie            
                """)
        submeniu2 = input()
    elif meniu1 == '3':
        print("Selectati campul de filtrare")
        print("""
        1.Task
        2.Dată
        3.Persoană responsabilă
        4.Categorie
        """)
        submeniu3 = input()
    elif meniu1 == '4':
        pass
    elif meniu1 == '5':
        pass
    elif meniu1 == '6':
        pass
    meniu_total = [meniu1, submeniu2, submeniu3]
    return meniu_total