import random


def ordenamiento_por_mezcla(lista):
    print(lista)
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        izquierda = ordenamiento_por_mezcla(izquierda)
        derecha = ordenamiento_por_mezcla(derecha)
        print(izquierda, '*' * 5, derecha)

        # iteradores para recorrer las dos sublistas
        i = 0
        j = 0

        # iterados para la lista principal
        k = 0

        # reconstruyendo la lista ya ordenada
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(lista)

    return lista


if __name__ == '__main__':
    tamanho_de_lista = int(input('De que tamanho sera la lista?: '))

    lista = [random.randint(0, 100) for i in range(tamanho_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)
