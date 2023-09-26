import matplotlib.pyplot as plt
import numpy as np
import unittest
import math

def accion_matrix(matriz, vector):
    'Función para calcular la "acción" de una matriz sobre un vector'

    filas_matriz, columnas_matriz = matriz.shape
    filas_vector, = vector.shape

    if columnas_matriz != filas_vector:
        return False

    resultado = np.zeros((filas_matriz))

    for j in range(filas_matriz):
        for k in range(columnas_matriz):
            resultado[j] += matriz[j, k] * vector[k]
    return resultado


def accion_matriz(matriz, vector):
    'Función para calcular la "acción" de una matriz sobre un vector con numeros complejos'

    filas_matriz, columnas_matriz = matriz.shape
    filas_vector, = vector.shape

    if columnas_matriz != filas_vector:
        return False

    resultado = np.zeros((filas_matriz), dtype=complex)

    for j in range(filas_matriz):
        for k in range(columnas_matriz):
            resultado[j] += matriz[j, k] * vector[k]
    return resultado


def canicas(matriz, vector, clicks):
    'Los experimentos de la canicas con coeficiente booleanos'

    cont = 0
    while cont < clicks:
        vector = accion_matrix(matriz, vector)
        cont += 1
    return vector

matriz = np.array([[0, 0, 0, 0, 0],[0, 0, 0, 1, 0],[1, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]])
vector = np.array([1, 2, 3, 4, 5])
clicks = 4
resultado = canicas(matriz, vector, clicks)
print("1", resultado)


def probabilistic(matriz, vector, clicks):
    'Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.'

    cont = 0
    while cont < clicks:
        vector = accion_matrix(matriz, vector)
        cont += 1
    return vector

matriz = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                   [(1/2), 0, 0, 0, 0, 0, 0, 0],
                   [(1/2), 0, 0, 0, 0, 0, 0, 0],
                   [0, (1/3), 0, 1, 0, 0, 0, 0],
                   [0, (1/3), 0, 0, 1, 0, 0, 0],
                   [0, (1/3), (1/3), 0, 0, 1, 0, 0],
                   [0, 0, (1/3), 0, 0, 0, 1, 0],
                   [0, 0, (1/3), 0, 0, 0, 0, 1]])
vector = np.array([1, 0, 0, 0, 0, 0, 0, 0])
clicks = 1
resultado = probabilistic(matriz, vector, clicks)
print("2", resultado)


def rendija(matriz, vector, clicks):
    'Experimento de las múltiples rendijas cuántico.'

    cont = 0
    while cont < clicks:
        vector = accion_matriz(matriz, vector)
        cont += 1
    return vector

matriz = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                   [(1/math.sqrt(2)), 0, 0, 0, 0, 0, 0, 0],
                   [(1/math.sqrt(2)), 0, 0, 0, 0, 0, 0, 0],
                   [0, (-1+1j/math.sqrt(6)), 0, 1, 0, 0, 0, 0],
                   [0, (-1-1j/math.sqrt(6)), 0, 0, 1, 0, 0, 0],
                   [0, (1-1j/math.sqrt(6)), (-1+1j/math.sqrt(6)), 0, 0, 1, 0, 0],
                   [0, 0, (-1-1j/math.sqrt(6)), 0, 0, 0, 1, 0],
                   [0, 0, (1-1j/math.sqrt(6)), 0, 0, 0, 0, 1]], dtype = complex)
vector = np.array([1, 0, 0, 0, 0, 0, 0, 0])
clicks = 1
resultado = rendija(matriz, vector, clicks)
print("3", resultado)


def graficar_vector(vector, nombre_archivo, formato='png'):
    'Grafica un vector como un diagrama de barras y lo guarda en un archivo de imagen.'

    fig, ax = plt.subplots()
    ax.bar(range(len(vector)), vector)
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor')
    ax.set_title('Diagrama de Barras')

    nombre_completo = f'{nombre_archivo}.{formato}'
    plt.savefig(nombre_completo, format=formato)

    plt.show()



matriz = np.array([[0, 0, 0, 0, 0],[0, 0, 0, 1, 0],[1, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]])
vector = np.array([1, 2, 3, 4, 5])
clicks = 4
resultado = canicas(matriz, vector, clicks)
mi_vector = resultado
nombre_archivo = 'grafico_vector'
formato = 'png'
graficar_vector(mi_vector, nombre_archivo, formato)
