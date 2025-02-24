import csv
import pandas
import pandas as pd

#Afiseaza taskurile din csv file cu un index pentru a putea alege taskul
csvData = pandas.read_csv('todo_taskuri.csv')
csvData.sort_values(["Categorie"])
print("Taskuri:\n")

print(csvData)
nr_task = str(input())
with open("todo_taskuri.csv", 'r') as filein:
    df = pd.read_csv(filein)
    df = df.iloc[nr_task:]
print(df)
