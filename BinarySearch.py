lista = [1, 3, 4, 6, 9]
buscar = 6

inicio = 0
fin = len(lista) - 1

while inicio <= fin:
    medio = (inicio + fin) // 2
    if lista[medio] == buscar:
        print(medio)
        break
    elif lista[medio] < buscar:
        inicio = medio + 1
    else:
        fin = medio - 1
