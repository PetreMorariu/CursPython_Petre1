import copy
import csv
import pandas
import todo_Meniul
import todo_edit



#  citire si adaugare categorie

def citire_categorii():
    print("Introduceti categoriile dorite cu virgula ',' intre ele:")
    categorii_for_csv = input().split(sep=",")
    return categorii_for_csv

def insert_categorii(categorie):
    with open("todo_categorii.csv", 'w+', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(categorie)
        print("Categoriile au fost salvate!\n")

#Verificare ca task nu mai exista deja
def verificare_task(task):
    my_validare = False
    with open("todo_taskuri.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if str(row) == str(task):
               my_validare = True
    return my_validare

# adaugare si verificare ca  un task nou are o categorie valida
def insert_new_task(task):
    while str(task[0]) != 'exit':
        categorie_de_verificat = copy.deepcopy(task[-1])
        with open("todo_categorii.csv", "r") as file:
            reader = csv.reader(file, delimiter=',')
            categorie_valida = 0
            for row in reader:
                for field in row:
                    if field == categorie_de_verificat:
                        categorie_valida = 1
        if categorie_valida == 1:
            with open("todo_taskuri.csv", 'a+', newline='') as file:
                csv_writer = csv.writer(file)
                if verificare_task(task):
                    print("Exista taskul!")
                else:
                    csv_writer.writerow(task)
        else:
            print("Nu exista categoria!")
        task = eliminare_spatii(input("New task\n").split(sep=','))
    else:
        print("S-au introdus task-urile valide!")

# meniul 1
def meniul1():
    with open("todo_categorii.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Categorii: ", row)

    csvData = pandas.read_csv('todo_taskuri.csv')
    csvData.sort_values(["Categorie"], axis=0, ascending=[True], inplace=True)
    print("Taskuri:\n")
    print(csvData)

# Functii de sortare din meniul 2
def sort_ascendendt(camp):
    csvData = pandas.read_csv('todo_taskuri.csv')
    csvData.sort_values([camp], axis=0, ascending=[True], inplace=True)
    print("Taskuri:\n")
    print(csvData)

def sort_descendent(camp):
    csvData = pandas.read_csv('todo_taskuri.csv')
    csvData.sort_values([camp], axis=0, ascending=[False], inplace=True)
    print("Taskuri:\n")
    print(csvData)

# Filtrarea datelor meniul 3

def filtrare_date(camp,rand):
    with open("todo_taskuri.csv", 'r') as filein, open("todo_filter.csv", "w+", newline='') as fileout:
        writer = csv.writer(fileout, delimiter=",")
        for row in csv.reader(filein, delimiter=","):
            if row[rand] == camp[0]:
                writer.writerow(row)
    with open("todo_filter.csv", 'r') as filein:
        reader = csv.reader(filein)
        for row in reader:
            print(row)

#Eliminare spatii nedorite si care mi-au dat batai de cap
def eliminare_spatii(task1):
    return [' '.join(string.split()) for string in task1]




if __name__ == '__main__':
 print("Y pentru adaugare date initiale sau orice pentru nu")
 y = input()
if y == 'Y':
    #adaugare de categorii in fisier citite de la tastatura
    insert_categorii(citire_categorii())

    #Adaug nume coloane in todo_taskuri.csv2
    with open("todo_taskuri.csv", 'w', newline='') as file:
        csv_writer = csv.writer(file,delimiter=',')
        csv_writer.writerow(['Task', 'Data', 'Responsabil', 'Categorie'])

     #adaugare de taskuri
    print("Introduceti task-urile dorite cu formatul:\nNume,Data,Responsabilul,Categorie\n 'exit' pentru terminare taskuri\n")
    insert_new_task(eliminare_spatii(input().split(sep=',')))

# meniu_selectat este lista cu valorile cu care vreau sa lucrez
meniu_selectat = todo_Meniul.meniu()
if meniu_selectat[0] == '1':
    meniul1()
if meniu_selectat[0] == '2':
    if meniu_selectat[1] == '1':
        sort_ascendendt("Task")
    if meniu_selectat[1] == '2':
        sort_descendent("Task")
    if meniu_selectat[1] == '3':
        sort_ascendendt("Data")
    if meniu_selectat[1] == '4':
        sort_descendent("Data")
    if meniu_selectat[1] == '5':
        sort_ascendendt("Responsabil")
    if meniu_selectat[1] == '6':
        sort_descendent("Responsabil")
    if meniu_selectat[1] == '7':
        sort_ascendendt("Categorie")
    if meniu_selectat[1] == '8':
        sort_descendent("Categorie")
if meniu_selectat[0] == '3':
    #Meniul 3->1 Task
    if meniu_selectat[2] == '1':
        print("Introduceti stringul de filtrare:")
        filtrare_date(eliminare_spatii(input().split()),0)
    #Meniul 3->2 Data
    if meniu_selectat[2] == '2':
        print("Introduceti stringul de filtrare:")
        filtrare_date(eliminare_spatii(input().split(sep=",")), 1)
    # Meniul 3->3 Responsabil
    if meniu_selectat[2] == '3':
        print("Introduceti stringul de filtrare:")
        filtrare_date(eliminare_spatii(input().split(sep=",")), 2)
    # Meniul 3->4 Categorie
    if meniu_selectat[2] == '4':
        print("Introduceti stringul de filtrare:")
        filtrare_date(input().split(), 3)
if meniu_selectat[0] == '4':
   print("New task:")
   task = eliminare_spatii(input().split(sep=","))
   insert_new_task(task)
if meniu_selectat[0] == '5':
    todo_edit.editare_task()
if meniu_selectat[0] == '6':
    pass



