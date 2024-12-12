# Algoritmo de burbuja con captura de pasos
def bubble_sort(data, states):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            states.append(data.copy())  # Guardar el estado actual
    return data

def quick_sort(data, left, right, states):
    if left >= right:  # Caso base: una sola pieza o índice cruzado
        return

    pivot_index = partition(data, left, right, states)  # Particionar el dataeglo
    quick_sort(data, left, pivot_index - 1, states)  # Ordenar la mitad izquierda
    quick_sort(data, pivot_index + 1, right, states)  # Ordenar la mitad derecha

def partition(data, left, right, states):
    pivot = data[right]  # Elegir el pivote (último elemento)
    i = left - 1  # Índice del menor

    for j in range(left, right):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]  # Intercambio
            states.append(data.copy())  # Capturar estado

    # Colocar el pivote en su lugar
    data[i + 1], data[right] = data[right], data[i + 1]
    states.append(data.copy())  # Capturar estado final del particionado
    return i + 1
