import csv
import pandas
import pandas as pd
from pandas.io.sas.sas_constants import row_length_offset_multiplier

def editare_task():

    # creaza un dictionar cu taskurile si le indexeaza
    data = pd.read_csv('todo_taskuri.csv')
    data_dict = data.to_dict(orient='index')
    print(data_dict)

    #Afiseaza taskurile din csv file cu un index pentru a putea alege taskul
    csvData = pandas.read_csv('todo_taskuri.csv')
    csvData.sort_values(["Categorie"])
    print("Taskuri:\n")
    print(csvData)

    print("Introduceti numarul taskului care va fii editat:")
    nr_task = int(input())

    print("Editati task-ul dorit:")
    edit_task = (input().split(sep=','))


    #editeaza task-ul dorit
    data_dict[nr_task] = {'Task':edit_task[0],
                          'Data':edit_task[1],
                          'Responsabil':edit_task[2],
                          'Categorie':edit_task[3]
                          }

    with open("todo_taskuri.csv", 'w', newline='') as file:
        csv_writer = csv.writer(file,delimiter=',')
        csv_writer.writerow(['Task', 'Data', 'Responsabil', 'Categorie'])

    for cheie in data_dict:
      my_rand = []
      for cheie2 in data_dict[cheie]:
         my_rand.append(data_dict[cheie][cheie2])
      with open("todo_taskuri.csv", 'a+',newline='') as fileout:
          my_writer = csv.writer(fileout)
          my_writer.writerow(my_rand)