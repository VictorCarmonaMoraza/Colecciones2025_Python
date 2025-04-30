print('***Manejo de Listas***')

mi_lista = [1, 2, 3, 4, 5]

print(f'{mi_lista} -> Lista original')

# Largo de la lista
print(f'El largo de la lista es: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 2: {mi_lista[2]}')

# Accedemos al ultimo indice de la lista
print(f'Accedemos al ultimo inidce de la lista {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'{mi_lista} --> Se agrego el elemento 6')

# Añadir un nuevo elemento en un inidce especifico
mi_lista.insert(2, 15)
print(f'{mi_lista} --> Se añadio el valor de 15 en el inidce 2')
