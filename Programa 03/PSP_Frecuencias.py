n = input('')
datos = [int (i) for i in n.split()]
f = input('')
maestros = [int (i) for i in f.split()]
rep = []
for i in range(0, datos[0]):
    rep.append(0)
    for fav in maestros:
        if fav == (i+1):
            rep[i] += 1

for i in range(0, datos[0]):
    print(f'{i+1}-{rep[i]}')