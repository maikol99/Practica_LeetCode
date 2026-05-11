x = int(input())

for i in range(x):
    anio = int(input())

    if anio % 100 == 0:
        siglo = anio // 100
    else:
        siglo = anio // 100 + 1

    print(siglo)

