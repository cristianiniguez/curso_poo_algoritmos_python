import random


def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - i - 1):  # O(n - 1) * O(n - i - 1) -> O(n**2)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == '__main__':
    tamanho_de_lista = int(input('De que tamanho sera la lista?: '))

    lista = [random.randint(0, 100) for i in range(tamanho_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)
