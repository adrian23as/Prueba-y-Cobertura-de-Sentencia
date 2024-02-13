def encontrar_maximo(lista):
    if not lista:
        return None  # Retorna None si la lista está vacía
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo


print(encontrar_maximo([]))  # Caso de prueba para lista vacía
print(encontrar_maximo([5]))  # Caso de prueba para lista con un elemento
print(encontrar_maximo([2, 8, 1, 6, 4]))