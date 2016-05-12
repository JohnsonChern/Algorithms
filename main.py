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

    
    l = random.sample(range(2**22), 2**20)

    start = time.clock()
    myselect.select(l, 0, len(l), 200)
    end = time.clock()

    print end - start

    """
    random_key = random.sample(range(100), 50)
    tree = brt.brtree()

    for key in random_key:
        tree.insert(brt.brnode(key))

    for key in random_key:
        tree.delete(tree.search(key))
    """

    """
    insert_time = []
    search_time = []
    delete_time = []
    k = 20
    k_l = range(1, k+1)

    for j in k_l:
        print j
        random_key  = random.sample(range(2**j*4),2**j)

        tree = brt.brtree()

        start = time.clock()
        for key in random_key:
            tree.insert(brt.brnode(key))
        end = time.clock()

        insert_time.append(end - start)

        start = time.clock()
        for key in random_key:
            tree.search(key)
        end = time.clock()

        search_time.append(end - start)

        start = time.clock()
        for key in random_key:
            tree.delete(tree.search(key))
        end = time.clock()

        delete_time.append(end - start)

    print insert_time
    print search_time
    print delete_time
    """

    """
    k = 20
    k_l = range(1, k+1)
    insert_time = [1.46053630893264e-05, 2.723702846387897e-05, 5.6053015099577e-05, 0.00010894811385551588, 0.0002751334614394731, 0.000569214420940775, 0.0012071135223556792, 0.0028046244526936243, 0.005970830326733815, 0.011083102147541008, 0.02096540660541362, 0.037402755913593086, 0.10567927570030741, 0.18540324223271004, 0.37864048543490025, 0.7574309718961236, 1.7575304462609478, 3.9813998727359703, 9.154499083414782, 20.144852438464053]
    search_time = [2.368437257728606e-06, 3.5526558865929037e-06, 8.289530402050136e-06, 1.8158018975919304e-05, 4.263187063911495e-05, 9.868488573869173e-05, 0.0002285541953708104, 0.0009288221445725676, 0.0014021148565753344, 0.0025713333828073573, 0.006891362940904332, 0.014552862730113414, 0.03659946094368016, 0.07129509307168946, 0.1580150285238795, 0.36874002295805175, 0.8234898449305179, 1.866524744642991, 4.226370101479642, 9.169558002238958]
    delete_time = [1.1447446745688261e-05, 2.842124709274327e-05, 4.618452652570783e-05, 0.00011131655111324448, 0.0002557912238346894, 0.0006055304588926135, 0.0012789561191734475, 0.0024568589153504735, 0.0050660872942814884, 0.0071578121323988, 0.015507342944978048, 0.04909217799911263, 0.07124377693110534, 0.14471270066584663, 0.3163719014919575, 0.6545989525191485, 1.3807381313661624, 3.0170630114837618, 6.348553832210431, 13.891831496741815]

    for i in range(len(insert_time)):
        insert_time[i] = log(insert_time[i], 10) + 6
        search_time[i] = log(search_time[i], 10) + 6
        delete_time[i] = log(delete_time[i], 10) + 6

    plt.figure(figsize=(16, 9))
    plt.plot(k_l, insert_time, label="insert_time", color="blue", linewidth=2)
    plt.plot(k_l, search_time, label="search_time", color="red", linewidth=2)
    plt.plot(k_l, delete_time, label="delete_time", color="green", linewidth=2)
    plt.xlabel("$log{n}$")
    plt.ylabel("$Running Time$")
    plt.legend()
    plt.show()
    """