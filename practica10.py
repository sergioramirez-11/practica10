print("Este programa es capaz de sumar todos los numeros ")

Numero = int(input("Anote los numeros que desea sumar:   "))

def sumainterativa(n):
    suma = 0

    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n

def sumarecursiva(n):
    if n <= 9:
        return n
    else:
        return sumarecursiva(n // 10) + n % 10
    
print(f"El resultado de la suma interatica es: {sumainterativa(Numero)}")
print(f"El resultado de la suma recursiva es: {sumarecursiva(Numero)}")
print ("Fin.")
