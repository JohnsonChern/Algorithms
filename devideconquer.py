import copy
from math import ceil, log


def binary_search(source, wanted, start, end):
    """
    Fuction Description:
        This function search for a certain object in a acsending sequence using binary search.
    Parameter Type:
        source:
            A acsending sequence.
            Its elements can be compared using operator < <= == >= >.
        wanted:
            The object you want to search.
            With the same type as elements in source.
    """
    middle = (start + end) / 2
    while end - start > 1:
        if source[middle] == wanted:

            # if source[middle] == wanted, search the left half in loops.
            # store the target's index in k_new.
            # keep searching recursively until the can't find the target.
            # this means the last k is the index that target first appears.
            k = middle
            end = middle
            while end > 0:
                k_new = binary_search(source, wanted, start, end)
                if k_new == -1:
                    return k
                k = k_new
                end = end / 2
            # this part deals with the case in which source[0] == wanted
            if source[start] == wanted:
                return start

        # if source[middle] > wanted, search the left part of the array
        elif source[middle] > wanted:
            return binary_search(source, wanted, start, middle)

        # else, i.e. source[middle] < wanted, search the right part
        else:
            return binary_search(source, wanted, middle + 1, end)

    # this part deals with the case in which start == end
    if source[middle] == wanted:
        return middle

    # target not found, return -1
    else:
        return -1




def naive_fibonacci(n):
    """
    Function Description:
        This function calculates the nth Fibonacci number, i.e. f(n)
        and return it.
        This function use the naive method to calculate.
    """
    if n < 0:
        print "wrong input!"
        return
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(2, n + 1, 1):
        # i starts from 2 to n
        c = a + b
        a = b
        b = c
    return c



def matrix_add(a, b):
    """
    Function Description:
        This function adds two matrices and return the result.
    """
    result = copy.deepcopy(a)
    n = len(a)
    for i in range(n):
        for j in range(n):
            result[i][j] += b[i][j]
    return result



def matrix_sub(a, b):
    """
    Function Description:
        This function calculates the result of (a - b) and return it.
    """
    result = copy.deepcopy(a)
    n = len(a)
    for i in range(n):
        for j in range(n):
            result[i][j] -= b[i][j]
    return result




def strassen(a, b):
    """
    Fuction Description:
        This function calculates the product of two matrices of size n*n,
        where n is a power number of 2, and returns the result.
    """
    n = len(a)

    if n <= 64:
        return naive_matrix_multiple(a, b)
    else:
        new_size = n / 2

        a11 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a12 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a21 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        a22 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        b11 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b12 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b21 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]
        b22 = [[0 for j in xrange(0, new_size)] for i in xrange(0, new_size)]

        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                a11[i][j] = a[i][j]
                a12[i][j] = a[i][j + new_size]
                a21[i][j] = a[i + new_size][j]
                a22[i][j] = a[i + new_size][j + new_size]

                b11[i][j] = b[i][j]
                b12[i][j] = b[i][j + new_size]
                b21[i][j] = b[i + new_size][j]
                b22[i][j] = b[i + new_size][j + new_size]

        m1 = strassen(matrix_add(a11, a22), matrix_add(b11, b22))
        m2 = strassen(matrix_add(a21, a22), b11)
        m3 = strassen(a11, matrix_sub(b12, b22))
        m4 = strassen(a22, matrix_sub(b21, b11))
        m5 = strassen(matrix_add(a11, a12), b22)
        m6 = strassen(matrix_sub(a21, a11), matrix_add(b11, b12))
        m7 = strassen(matrix_sub(a12, a22), matrix_add(b21, b22))

        c11 = matrix_add(matrix_sub(matrix_add(m1, m4), m5), m7)
        c12 = matrix_add(m3, m5)
        c21 = matrix_add(m2, m4)
        c22 = matrix_add(matrix_add(matrix_sub(m1, m2), m3), m6)

        result = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                result[i][j] = c11[i][j]
                result[i][j + new_size] = c12[i][j]
                result[i + new_size][j] = c21[i][j]
                result[i + new_size][j + new_size] =c22[i][j]

        return result





def strassen_matrix_multiple(a, b):
    """
    Fuction Description:
        This function extends a and b to the size of next power of 2.
        Then it calls strassen method to calculate the temporary result.
        At last it takes the former n*n matrix and returns it.
        This function uses strassen algorithm.
    """
    n = len(a)
    m = 2**int(ceil(log(n,2)))

    extended_a = [[0 for j in xrange(0, m)] for i in xrange(0, m)]
    extended_b = [[0 for j in xrange(0, m)] for i in xrange(0, m)]

    for i in xrange(0, n):
        for j in xrange(0, n):
            extended_a[i][j] = a[i][j]
            extended_b[i][j] = b[i][j]

    extended_result = strassen(extended_a, extended_b)

    result = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            result[i][j] = extended_result[i][j]

    return result



def naive_matrix_multiple(a, b):
    """
    Function Description:
        This function calculate the product of matrix a and b
        and return the result.
        This function uses naive method with time complexity n^3
    """
    result = copy.deepcopy(a)
    n = len(a)
    for i in range(n):
        for j in range(n):
            result[i][j] = 0
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_pow(matrix, n):
    """
    Function Description:
        This function calculate the nth power of matrix.
    Parameter Type:
        n: the power of the matrix
        matrix: given in the following form
        [
            [a11, a12, ..., a1n],
            [a21, a22, ..., a2n],
            ...
            [an1, an2, ..., ann]
        ]
    Return Type:
        Return the result of the power with the same format as
        matrix.
    """
    if n == 1:
        return matrix

    if n % 2 == 0:
        temp = matrix_pow(matrix, n / 2)
        return naive_matrix_multiple(temp, temp)
    else:
        temp = matrix_pow(matrix, n / 2)
        return naive_matrix_multiple(matrix, 
            naive_matrix_multiple(temp, temp))


def la_fibonacci(n):
    """
    Function Description:
        This function calculate the nth Fibonacci number, i.e. f(n)
        and return it.
        This function use linear algebra method, i.e.:

                                        n
        f(n + 1)    f(n)         1   1
                             =    
          f(n)    f(n - 1)       1   0

        To calculate the nth power of the 2*2 matrix, we apply
        devide and conquer method.

    """
    return matrix_pow([[1, 1], [1, 0]], n)[0][0]
