import sort
import myselect
import devideconquer
import random
import copy
import matplotlib.pyplot as plt
import time
import timeit
import numpy
import brtree as brt
from math import log, floor

def test(a, b):
    print a == b

if __name__ == "__main__":

    

    """
    plt.figure(figsize=(12, 9))
    plt.scatter(ran, random_select, label="random", color="blue")
    plt.scatter(ran, normal_select, label="normal", color="red")
    plt.plot(ran, random_p(ran), label="random_fit", color="blue", linewidth=2)
    plt.plot(ran, normal_p(ran), label="normal_fit", color="red", linewidth=2)
    plt.xlabel("$log{n}$")
    plt.ylabel("$\log{Running Time}$")
    plt.text(3,18,"k = %s" % normal_fit[0],
        bbox={'facecolor':'red','alpha':0.5,'pad':10})
    plt.text(15, 13,"k = %s" % random_fit[0],
        bbox={'facecolor':'blue','alpha':0.5,'pad':10})
    plt.legend()
    plt.show()
    """