import time
import sys

# Hallando el factorial de un número


def factorial_iterativo(n):
    '''
    Factorial de forma iterativa
    '''
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_recursivo(n):
    '''
    Factorial de forma recursiva
    '''
    if n == 1:
        return 1
    return n * factorial_recursivo(n - 1)


if __name__ == "__main__":
    sys.setrecursionlimit(10**5)

    n = 100000

    comienzo = time.time()
    factorial_iterativo(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    print(final - comienzo)
