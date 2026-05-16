a = int(input())

if 0 < a < 1000000:

    print(a)

    nota100 = a // 100
    a = a % 100

    nota50 = a // 50
    a = a % 50

    nota20 = a // 20
    a = a % 20

    nota10 = a // 10
    a = a % 10

    nota5 = a // 5
    a = a % 5

    nota2 = a // 2
    a = a % 2

    nota1 = a

    print(f"{nota100} nota(s) de R$ 100,00")
    print(f"{nota50} nota(s) de R$ 50,00")
    print(f"{nota20} nota(s) de R$ 20,00")
    print(f"{nota10} nota(s) de R$ 10,00")
    print(f"{nota5} nota(s) de R$ 5,00")
    print(f"{nota2} nota(s) de R$ 2,00")
    print(f"{nota1} nota(s) de R$ 1,00")