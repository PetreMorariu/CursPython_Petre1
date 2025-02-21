import csv

change = 'piupiu'
with open("todo_taskuri_provizoriu.csv", 'r') as filein:
    dt = csv.reader(filein)
    print(dt)
    up_dt = []
    for r in dt:
        print(r)
        if r[0] == 'Task':
            pass
        else:
            if r[3] == 'avioane':
                row = { 'Task': r[0],
                        'Data': r[1],
                        'Responsabil': r[2],
                        'Categorie': change}
                up_dt.append(row)
            else:
                row = {'Task': r[0],
                       'Data': r[1],
                       'Responsabil': r[2],
                       'Categorie': r[3]}
                up_dt.append(row)
    print(up_dt)
with open("todo_taskuri_provizoriu1.csv", 'w+', newline='') as fileout:
    headers = ['Task', 'Data', 'Responsabil', 'Categorie']
    data = csv.DictWriter(fileout, delimiter=',', fieldnames=headers)
    data.writerow(dict((heads, heads) for heads in headers))
    data.writerows(up_dt)