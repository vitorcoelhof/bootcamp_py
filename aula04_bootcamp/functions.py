#ordenação na mão

lista_de_numeros = [64, 34, 25, 12, 22, 11, 90]

def ordenar_lista(numeros): 
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(lista_de_numeros)):
        for j in range(i + 1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]
    return nova_lista_de_numeros

nova_lista = ordenar_lista(lista_de_numeros)

print(nova_lista)


