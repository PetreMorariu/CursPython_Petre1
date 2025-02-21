#Sa se inlocuiasca in textul alocat variabilei "var_string", sirurile de caractere aferente pozitiilor de start si stop,
# cu string-urile din lista "patches"

var_string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# [start, end, patch]
patches = [[4, 14, "Conquistador"], [25, 31, "King"], [42, 49, "Palace"]]
for n in patches:
    var_string2 = var_string.replace(format(var_string[n[0]:n[1]]), n[2])
    print(var_string2)