"""
Si tenemos una lista "A" de numeros enteros tanto positivos o negativos
definienimos la maxima sub-lista "B" como una sub-lista de "A" de elementos contiguos que nos
dan la suma de mayor magnitud. Por ejemplo si tenemos la lista A=[1, 3, -5, 6, 9]
la maxima sub-lista sera B=[6,9] -> A[3:4]. La suma es 15


Usando la funcion ya definida "get_maximum_crossing_subarray" como funcion auxiliar
definir la funcion(!!!!!ya esta definida con un bloque vacio abajo):
get_maximum_subarray(A: tuple, low: int, high: int) -> Union[int, int, float]

Donde:
A: la lista original con numero de elementos pares(2, 8, 14, etc). Esto por simplicidad.
low: indice inferior de la lista(para la primer invocacion sera 0)
high: indice superior de la lista(para la primera invocacion sera len(A) - 1)


Esta funcion debera retornar la maximo sub-lista contigua que nos de la mas grande suma.
Retornara una tupla como sigue -> (indice_inferior, indice_superior, suma_de_los_elementos)

Nota: En la parte inferior se encuentra el codigo donde se manda llamar esta funcion
    que tienes que definir, ya con una lista de ejemplo

"""


from typing import Union
import sys


def get_maximum_crossing_subarray(A: tuple, low: int, mid: int, high: int) -> Union[int, int, float]:
    """
    Return the contiguos sub array using a midpoint to saparate A into 2 subarrays.
    :param A: (tuple) array where we search the max sub array.
    :param low: (int) the low index of A where we must search.
    :param mid: (int) The mid of the array.
    :param high: (int) The high index of A where we must search.
    :return: (tuple) tuple where 3 values, the first 2 values are the
    low and high index of the maximum sub array found and the 3th value is 
    the sum maximum sub array sum.
    :rtype: Union(int, int, float)
    """
    left_sum = -sys.maxsize
    sum = 0
    index_left = mid
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            index_left = i

    right_sum = -sys.maxsize
    sum = 0
    index_right = mid
    for j in range(mid + 1, high + 1, 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            index_right = j

    return (index_left, index_right, left_sum + right_sum)


def get_maximum_subarray(A: tuple, low: int, high: int) -> Union[int, int, float]:
    """
    Return the contiguos sub array of A whose value
    have the largest sum. This function apply the method
    divide and conquer(recursive function).
    :param A: List of integers.
    :param low: The lowest index of A.
    :param high: The highest index of A.
    :return: (tuple) tuple with the low and high index of the new sub array
    that containt the largest sum. for example for the array A=[1, 3, -5, 6, 9]
    the tuple returned will be (3, 4, 15) where 3 and 4 and the index of the subarray
    A[3:4] and the 15 is the sum of the subarray A[3:4].
    Notice that the array A must be a power size of 2 to ensure that n/2 is an integer.
    :rtype: Union[int, int, float]
    """
    pass # <here the definition of the function.>






if __name__ == "__main__":
    """
    all the list the first element is the index 0 and the last
    index is the A.length - 1
    """
    A = [1, 3, -3, -4, -3, 3, 3, 4]
    low_index, high_index = 0, len(A) -1
    idx_low, idx_high, sum = get_maximum_subarray(A, low_index, high_index)
    max_subarray = A[idx_low:idx_high]
    print(f"the maximum sub array of {A} is {max_subarray} with the idx [{idx_low}:{idx_high}] and the sum is {sum}" )