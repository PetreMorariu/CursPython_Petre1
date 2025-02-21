
if __name__ == '__main__':
    pass
while True:
    try:
        CNP = int(input("Introduceti CNP-ul pentru validare:"))
        break
    except ValueError:
        print("Oops! Ati introdus altceva decat cifre. Mai incercati...")

CNP_cnt = CNP
cnt = 0
while CNP_cnt > 0:
    CNP_cnt //= 10 #floor division
    cnt += 1

if cnt != 13:
    print("CNP-ul nu este valid: nu ati introdus 13 cifre")
    exit()

CNP_l1 = [CNP]
CNP_list_final = [int(digit) for digit in str(CNP_l1[0])]

#validam luna LL
list_ll = CNP_list_final[3:5].copy()
if list_ll[0] == 1:
    if list_ll[1] > 2:
        print("CNP-ul nu este valid: ati introdus gresit luna")
        exit()
if list_ll[0] > 1:
    print("CNP-ul nu ese valid: ati introdus gresit luna")
    exit()

#validam ziua ZZ
list_zz = CNP_list_final[5:7].copy()
if list_zz[0] > 3:
    print("CNP-ul nu este valid: ati introdus gresit ziua")
    exit()
else:
    if list_zz[0] == 3 and list_zz[1] > 2:
        print("CNP-ul nu este valid: ati introdus gresit ziua")
        exit()

#validam judetul JJ
list_JJ = CNP_list_final[7:9].copy()
numar_JJ = int(''.join(map(str, list_JJ)))
list_JJ2 = list(range(1,46))
list_JJ2.append(51)
list_JJ2.append(52)

if numar_JJ in list_JJ2:
    pass
else:
    print("CNP=ul nu este valid: ati introdus gresit indexul judetului")
    exit()

#validam C
list_control = [2, 7, 9, 1 ,4, 6, 3, 5, 8, 2, 7, 9]
n = 0
list_multiply = []
while n < 12:
    s_control = CNP_list_final[n] * list_control[n]
    list_multiply.append(s_control)
    n = n + 1

control_adunare = 0
for x in list_multiply:
   control_adunare = control_adunare + x

dec_result = control_adunare % 11
if dec_result == CNP_list_final[12]:
    print("CNP-ul este valid!")
else:
    print("CNP-ul nu este valid: numarul de control nu este valid")












