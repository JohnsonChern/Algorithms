import sort
import devideconquer
import random
import copy
import matplotlib.pyplot as plt
import time
import timeit
from math import log

if __name__ == "__main__":

    a = [random.randint(0, 5) for i in xrange(16)]
    b = random.randint(0, 5)
    sort.insert_sort(a)
    print a
    print b
    print devideconquer.binary_search(a, b, 0, len(a))

"""
    k = range(1,11,1)
    strassen_time = [0 for i in xrange(10)]
    naive_time = [0 for i in xrange(10)]

    for i in range(9, 10, 1):
        n = pow(2, i + 1)
        matrix = [[random.randint(0,10) for j in xrange(n)] for k in xrange(n)]
        t = time.clock()
        devideconquer.strassen_matrix_multiple(matrix, matrix)
        t1 = time.clock()
        strassen_time[i] = (t1 - t)
        t = time.clock()
        devideconquer.naive_matrix_multiple(matrix, matrix)
        t1 = time.clock()
        naive_time[i] = (t1 - t)

    print strassen_time, naive_time

    plt.figure(figsize=(16,8))
    plt.plot(k,la_time,label="Linear Algebra Method",color="red",linewidth=2)
    plt.plot(k,naive_time,"b--",label="Naive Method")
    plt.xlabel("log(n)")
    plt.ylabel("Running Time($10^{-6}$s)")
    plt.title("Fibonacci Time Analysis")
    plt.xlim(9, 21)
    plt.legend()
    plt.show()
"""