
n = int(input())

horas = n // 3600
n = n % 3600

minutos = n // 60
segundos = n % 60

print(f"{horas}:{minutos}:{segundos}")


