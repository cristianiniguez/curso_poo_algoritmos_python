import random
import time


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


def busqueda_binaria(lista, comienzo, final, objetivo):
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    tamanho_de_lista = int(input('De que tamanho sera la lista?: '))
    objetivo = int(input('Que numero quieres encontrar?: '))

    lista = sorted([random.randint(0, 100) for i in range(tamanho_de_lista)])

    # Usando busqueda lineal
    comienzo = time.time()
    encontrado_lineal = busqueda_lineal(lista, objetivo)
    final = time.time()
    tiempo_busqueda_lineal = final - comienzo

    # Usando busqueda binaria
    comienzo = time.time()
    encontrado_binaria = busqueda_binaria(lista, 0, len(lista), objetivo)
    final = time.time()
    tiempo_busqueda_binaria = final - comienzo

    # Resultados
    razon = tiempo_busqueda_lineal / tiempo_busqueda_binaria
    print(f'Lineal / Binaria = {razon}')
    print(f'Gana busqueda {"binaria" if razon > 1 else "lineal"}')
