import random

# Generar una lista de 10 números al azar del 1 al 100
numeros = [random.randint(1, 100) for _ in range(10)]

print("Números generados:", numeros)

# Sacar promedio
promedio = sum(numeros) / len(numeros)
print("Promedio:", promedio)

# Identificar numero primo
def es_primo(num):
    for n in range(2,num):
        if num%n == 0:
            return False
    return True

cantidad_primos = sum(1 for num in numeros if es_primo(num))
print("Cantidad de números primos:", cantidad_primos)

# Identificar numeros pares
cantidad_pares = sum(1 for num in numeros if num % 2 == 0)
print("Cantidad de números pares:", cantidad_pares)

# Mustrar el número mayor
numero_mayor = max(numeros)
print("Número mayor:", numero_mayor)

# Mustrar el número menor
numero_menor = min(numeros)
print("Número menor:", numero_menor)