a, b, c = map(float, input().split())

pi = 3.14159

a_triangulo = (a * c) / 2
a_circulo = pi * (c ** 2)
a_trapecio = ((a + b) * c) / 2
a_cuadrado = b ** 2
a_rectangulo = a * b

print(f"TRIANGULO: {a_triangulo:.3f}")
print(f"CIRCULO: {a_circulo:.3f}")
print(f"TRAPEZIO: {a_trapecio:.3f}")
print(f"QUADRADO: {a_cuadrado:.3f}")
print(f"RETANGULO: {a_rectangulo:.3f}")